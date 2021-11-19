from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    similitude=0
    cpt=0
    for i in liste_modeles:
        im_bin=image.binarisation(S)
        im_loc=im_bin.localisation()
        im_res=im_loc.resize(i.H,i.W)
        if im_res.similitude(i)>similitude:
            similitude=im_res.similitude(i)
            res=cpt
        cpt+=1
    return res
        
        
        

