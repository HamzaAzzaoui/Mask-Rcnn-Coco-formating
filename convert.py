import os
import urllib.request
import shutil
import math
import json 



def bbox(ann):
    x=[]
    y=[]
    for f in range(len(ann[0])):
        if f%2==0:
            x.append(ann[0][f])
        else:
            y.append(ann[0][f])

    minx=min(x)
    maxx=max(x)
    miny=min(y)
    maxy=max(y)

    return [minx, miny, maxx, maxy]

def processVertices(Vertices):
    liste=[]
    for v in Vertices:
        x=v['x']
        y=v['y']
        liste.append(x)
        liste.append(y)
    liste=[liste]
    return liste

def area(ann):
    x=[]
    y=[]
    for f in range(len(ann[0])):
        if f%2==0:
            x.append(ann[0][f])
        else:
            y.append(ann[0][f])

    area=0
    n=len(x)
    for i in range(len(x)):
        j=(1+i) % n 
        area+= x[i]*y[j]
        area-= x[j]*y[i]
    area=abs(area)/2
    return area


## Path to the folder with json files

Json_path="/home/hamza/Desktop/json_file" ## TODO

coco_format={}


coco_format['info']={}
coco_format['info']['contributor']="Hamza"
coco_format['info']['date_created']='TODO'
coco_format['info']['description']='TODO'
coco_format['info']['url']='TODO'
coco_format['info']['version']=1
coco_format['info']['year']=2018



coco_format['images']=[]
coco_format['annotations']=[]
coco_format['categories']=[]
##Filling categories:

# It's better to put a loop here: This is just for clarification:

coco_format['categories'].append({})
coco_format['categories'].append({})
coco_format['categories'].append({})


coco_format['categories'][0]['supercategory']='class1'
coco_format['categories'][0]['id']=1
coco_format['categories'][0]['name']='class1'

coco_format['categories'][1]['supercategory']='class2'
coco_format['categories'][1]['id']=2
coco_format['categories'][1]['name']='class3'

coco_format['categories'][2]['supercategory']='class3'
coco_format['categories'][2]['id']=3
coco_format['categories'][2]['name']='class3'

## Filling images and annotations:

image_id=1
label_id=1
for f in os.listdir(Json_path):


    json_file=os.path.join(Json_path,f)
    own=json.load(open(json_file))
    labels=own['labels']
    ## Filling images:

    image={}
    image['file_name']=f[:-5]+'.jpg' 
    image['height']='TODO'   
    image['width']='TODO'    
    image['id']=image_id
    image['coc_url']='TODO'
    image['date_captured']='TODO'
    image['flickr_url']='TODO'
    coco_format['images'].append(image)
    

    ##Filling annotations:

    for l in labels:
        if l['label_type']=='box':
            continue
        label={}
        label['id']=label_id
        label['image_id']=image_id
        label['iscrowd']=0

        if l['label_class']=='class1':
            label['category_id']=1
        if l['label_class']=='class2':
            label['category_id']=2
        if l['label_class']=='class3':
            label['category_id']=3
        
        v=processVertices(l['vertices'])

        label['segmentation']=v 
        
        label['area']=area(v)
        label['bbox']=bbox(v)

        label_id+=1

        print("label", label)
        coco_format['annotations'].append(label)

    image_id+=1


with open("Path/to/jsonfile/file.json",'w') as fp:
    json.dump(coco_format,fp)

































