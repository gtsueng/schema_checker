import json
import pathlib
import os

def check_files(script_path):
    draft_folder = os.path.join(script_path,'drafts/')
    edited_folder = os.path.join(script_path,'edited/')
    draftlist = os.listdir(draft_folder)
    editlist = os.listdir(edited_folder)
    newfiles = [x for x in draftlist if x not in editlist]
    return(draft_folder,edited_folder,newfiles)

def create_dummy_class(eachclass):
    eachclass_info = eachclass.split(":")
    namespace = rangeid_info[0]
    classname = rangeid_info[1]
    dummy_dict = {
      "@id": eachclass,
      "@type": "rdfs:Class",
      "rdfs:comment": "A dummy class to enable avoid referencing issues",
      "rdfs:label": classname,
      "rdfs:subClassOf": {
        "@id": "schema:CreativeWork"
      }
    }
    return(dummy_dict)

def check_draft_schema(script_path):
    draft_folder,edited_folder,newfiles = check_files(script_path)
    for eachfile in newfiles:
        with open(os.path.join(draft_folder,eachfile),'r') as tempinfile:
            tmpjson = json.load(tempinfile)
        cleanjson = {}
        cleanjson['@context']=tmpjson['@context']
        graphlist = []
        rangelist = []
        for x in tmpjson['@graph']:
            graphlist.append(x)
            if x["@type"]=="rdf:Property":
                tmprangelist = x["schema:rangeIncludes"]
                for eachhit in tmprangelist:
                    if (eachhit['@id'] not in rangelist) and ("schema:" not in eachhit['@id']):
                        rangelist.append(eachhit['@id'])
        for eachclass in rangelist:
            dummy_dict = create_dummy_class(eachclass)
            graphlist.append(dummy_dict)
        cleanjson['@graph']=graphlist
        with open(os.path.join(edited_folder,eachfile),'w+') as tmpoutfile:
            tmpoutfile.write(json.dumps(cleanjson))

## Main
script_path = pathlib.Path(__file__).parent.absolute()
check_draft_schema(script_path)