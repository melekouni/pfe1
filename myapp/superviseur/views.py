from django.shortcuts import render, redirect , HttpResponse
from .models import *
from django.contrib.gis.geos import GEOSGeometry
from .forms import projectform , Form_client
import json
from .status import result
from django.contrib.auth.decorators import login_required
@login_required
def stocker_polygone(request):
    proj=request.user
    projects = project.objects.filter(client__superviseur__nom=proj.username)
    if request.method == 'POST':
        polygonString = request.POST.get('cord')
        polygonJson = json.loads(polygonString)
        
        id_project = request.POST.get('id_proj')
        proj = project.objects.get(id=id_project)
        polygon_name = request.POST.get('nom')
        for poly in polygonJson:
            polygon = GEOSGeometry(json.dumps(poly))
            instance = myPolygon( geom=polygon , nom=polygon_name , project=proj )
            instance.save()
        return redirect('node', id= id_project )
    return render(request, 'map.html',{'project':projects})
@login_required
def superviser(request):
   
    return render(request, 'superviser.html')
@login_required
def node(request,id):
        
        id_poly = myPolygon.objects.filter(project=id)
        id_proj = project.objects.get (id = id)
        print(id_proj)

        polysFromDB = myPolygon.objects.filter(project=id).values() 
        polys = []
        for pol in polysFromDB:
            polys.append(json.loads(pol['geom'].json))
        print(polys)
        nodes=[]
        nodess = point.objects.filter(project=id).values()
        for p in nodess:
            nodes.append(json.loads(p['cord'].json))
        print( nodes )
        if request.method == 'POST':
            points = request.POST.get('points')
            nom = request.POST.get('nom')
            id_polys =request.POST.get('id_poly')
            ref = request.POST.get('ref') 
          
            print(id_polys)
            poly = myPolygon.objects.get(id =id_polys)
            print(poly)
            points = GEOSGeometry(points)

            instance = point(cord=points,nom=nom,parcelle=poly , project=id_proj , référence=ref)
            instance.save()

            return redirect('node',id=id)
        
     
        return render(request, 'nodes.html', {'polys': polys,'id_poly':id_poly, 'nodes':nodes} )


@login_required
def compte(request):
         user=request.user.username
         if request.method == 'POST':
            formulaire = Form_client(request.POST)
            if formulaire.is_valid():
                
                formulaire.enregistrer(user)
              
                
                return redirect('création_project')
            
            return render(request, 'signup.html', {'form': formulaire  })
         return render(request, 'signup.html', {'form': Form_client()})
   
@login_required
def all_project(request):
    user=request.user
    print(user.username)
    project_list = project.objects.filter(client__superviseur__nom =user.username)
    print(project_list)
    return render (request, 'consult.html', {'project_list':project_list}  )





def delete(request,id):
    user=request.user
    print(user.username)
    project_list = project.objects.filter(client__superviseur__nom =user.username)
   
    if request.method == 'POST':
         sp=project.objects.get(id=id)
         print(sp)
         sp.delete()
         
         
    return render (request, 'consult.html',{'project_list':project_list})
   
@login_required    
def création_project(request):
    sv= request.user
    clientss = client.objects.filter(superviseur__nom=sv.username)
    
    form = projectform()
    if request.method =="POST": 
        form = projectform(request.POST)
        print(form)
        if form.is_valid():
            id=request.POST.get('id')
            nom=request.POST.get('nom')
            region=request.POST.get('region')
            d_deb=request.POST.get('date-deb')
            d_fin=request.POST.get('date-fin')
            id_clients = request.POST.get('id_client')
            id_client =client.objects.get(id= id_clients)
            print(id_client)
            data=project(id=id, nom=nom , region=region, client=id_client,dat_deb=d_deb,dat_fin=d_fin)
            data.save()
        return redirect('stocker_polygone')
    context = {'form':form , 'clientss':clientss}
    return render(request, 'création_project.html',context)





@login_required
def get_polygone(request,id):
        
       
        polysFromDB = myPolygon.objects.filter(project=id).values() 
        polys = []
        for pol in polysFromDB:
            polys.append(json.loads(pol['geom'].json))
        

        polysFromDB = point.objects.filter(project=id).values() 
        nodes = point.objects.filter(project=id)
        points = []
        for pol in polysFromDB:
          points.append(json.loads(pol['cord'].json))

        polygon=myPolygon.objects.filter(project=id)
        pol=polygon[0].geom.json
        
        data_list= []
        for n in nodes :
             ds = Post.objects.filter(node=n).order_by('-id').first()
             print(ds,'h')
             data_list.append(ds)

             
        return render(request, 'map2.html', {'polys':polys , 'points':points , 'pol':pol ,'data_list':data_list })
