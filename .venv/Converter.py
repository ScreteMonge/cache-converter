import json
import os.path
from tkinter import filedialog


def main():
    directory = filedialog.askdirectory()
    if directory == "":
        print("Directory is empty or isn't 'dump.' Canceling program.")
        return

    perform_kit = True
    perform_obj = True
    perform_spotanim = True
    perform_seq = True
    perform_item = True
    perform_npc = True

    if perform_kit:
        kit_file_list = []
        kit_path = directory + '/kits/'
        print("Found ", kit_path, ", beginning dump.")
        for kit_filenames in os.walk(kit_path):
            kit_file_list.append(kit_filenames)

        kit_list = []
        for i in range(len(kit_filenames[2])):
            try:
                data = json.load(open(kit_path + kit_filenames[2][i], encoding='utf-8'))
                id = data.get('id')
                bodyPartId = data.get('bodyPartId')
                models = data.get('models')
                chatheadModels = data.get('chatheadModels')
                recolorToReplace = data.get('recolorToReplace')
                recolorToFind = data.get('recolorToFind')
                kit_final = {'id': id, 'bodyPartId': bodyPartId, 'models': models, 'chatheadModels': chatheadModels,
                             'recolorToReplace': recolorToReplace, 'recolorToFind': recolorToFind}
                kit_list.append(kit_final)
            except Exception:
                pass

        kit_out = open("kit.json", "w")
        json.dump(kit_list, kit_out, indent=2)
        kit_out.close()

    if perform_obj:
        obj_file_list = []
        obj_path = directory + '/object_defs/'
        print("Found ", obj_path, ", beginning dump.")
        for obj_filenames in os.walk(obj_path):
            obj_file_list.append(obj_filenames)

        obj_list = []
        for i in range(len(obj_filenames[2])):
            try:
                data = json.load(open(obj_path + obj_filenames[2][i], encoding='utf-8'))
                id = data.get('id')
                name = data.get('name')
                objectModels = data.get('objectModels')
                objectTypes = data.get('objectTypes')
                modelSizeX = data.get('modelSizeX')
                modelSizeY = data.get('modelSizeY')
                modelSizeZ = data.get('modelSizeHeight')
                ambient = data.get('ambient')
                contrast = data.get('contrast')
                recolorToReplace = data.get('recolorToReplace')
                recolorToFind = data.get('recolorToFind')
                textureToReplace = data.get('textureToReplace')
                retextureToFind = data.get('retextureToFind')
                obj_final = {'id': id,
                             'name': name,
                             'objectModels': objectModels,
                             'objectTypes': objectTypes,
                             'modelSizeX': modelSizeX,
                             'modelSizeY': modelSizeY,
                             'modelSizeZ': modelSizeZ,
                             'ambient': ambient,
                             'contrast': contrast,
                             'recolorToReplace': recolorToReplace,
                             'recolorToFind': recolorToFind,
                             'textureToReplace': textureToReplace,
                             'textureToFind': retextureToFind
                             }
                obj_list.append(obj_final)
            except Exception:
                pass

        obj_out = open("object_defs.json", "w")
        json.dump(obj_list, obj_out, indent=2)
        obj_out.close()

    if perform_spotanim:
        spotanim_file_list = []
        spotanim_path = directory + '/spotanims/'
        print("Found ", spotanim_path, ", beginning dump.")
        for spotanim_filenames in os.walk(spotanim_path):
            spotanim_file_list.append(spotanim_filenames)

        spotanim_list = []
        for i in range(len(spotanim_filenames[2])):
            try:
                data = json.load(open(spotanim_path + spotanim_filenames[2][i], encoding='utf-8'))
                id = data.get('id')
                modelId = data.get('modelId')
                animationId = data.get('animationId')
                resizeX = data.get('resizeX')
                resizeY = data.get('resizeY')
                ambient = data.get('ambient')
                contrast = data.get('contrast')
                recolorToReplace = data.get('recolorToReplace')
                recolorToFind = data.get('recolorToFind')
                spotanim_final = {'id': id,
                                  'modelId': modelId,
                                  'animationId': animationId,
                                  'resizeX': resizeX,
                                  'resizeY': resizeY,
                                  'ambient': ambient,
                                  'contrast': contrast,
                                  'recolorToReplace': recolorToReplace,
                                  'recolorToFind': recolorToFind}
                spotanim_list.append(spotanim_final)
            except Exception:
                pass

        spotanim_out = open("spotanims.json", "w")
        json.dump(spotanim_list, spotanim_out, indent=2)
        spotanim_out.close()

    if perform_seq:
        seq_file_list = []
        seq_path = directory + '/sequences/'
        print("Found ", seq_path, ", beginning dump.")
        for seq_filenames in os.walk(seq_path):
            seq_file_list.append(seq_filenames)

        seq_list = []
        for i in range(len(seq_filenames[2])):
            try:
                data = json.load(open(seq_path + seq_filenames[2][i], encoding='utf-8'))
                id = data.get('id')
                leftHandItem = data.get('leftHandItem')
                rightHandItem = data.get('rightHandItem')
                seq_final = {
                    'id': id,
                    'rightHandItem': rightHandItem,
                    'leftHandItem': leftHandItem
                }
                seq_list.append(seq_final)
            except Exception:
                pass

        seq_out = open("sequences.json", "w")
        json.dump(seq_list, seq_out, indent=2)
        seq_out.close()

    if perform_item:
        item_file_list = []
        item_path = directory + '/item_defs/'
        print("Found ", item_path, ", beginning dump.")
        for item_filenames in os.walk(item_path):
            item_file_list.append(item_filenames)

        item_list = []
        for i in range(len(item_filenames[2])):
            try:
                data = json.load(open(item_path + item_filenames[2][i], encoding='utf-8'))
                id = data.get('id')
                name = data.get('name')
                inventoryModel = data.get('inventoryModel')
                maleModel0 = data.get('maleModel0')
                maleModel1 = data.get('maleModel1')
                maleModel2 = data.get('maleModel2')
                maleOffset = data.get('maleOffset')
                femaleModel0 = data.get('femaleModel0')
                femaleModel1 = data.get('femaleModel1')
                femaleModel2 = data.get('femaleModel2')
                femaleOffset = data.get('femaleOffset')
                maleHeadModel = data.get('maleHeadModel')
                maleHeadModel2 = data.get('maleHeadModel2')
                femaleHeadModel = data.get('femaleHeadModel')
                femaleHeadModel2 = data.get('femaleHeadModel2')
                resizeX = data.get('resizeX')
                resizeY = data.get('resizeY')
                resizeZ = data.get('resizeZ')
                colorReplace = data.get('colorReplace')
                colorFind = data.get('colorFind')
                textureReplace = data.get('textureReplace')
                textureFind = data.get('textureFind')

                item_final = {'id': id,
                              'name': name,
                              'inventoryModel': inventoryModel,
                              'maleModel0': maleModel0,
                              'maleModel1': maleModel1,
                              'maleModel2': maleModel2,
                              'maleOffset': maleOffset,
                              'femaleModel0': femaleModel0,
                              'femaleModel1': femaleModel1,
                              'femaleModel2': femaleModel2,
                              'femaleOffset': femaleOffset,
                              'maleHeadModel': maleHeadModel,
                              'maleHeadModel2': maleHeadModel2,
                              'femaleHeadModel': femaleHeadModel,
                              'femaleHeadModel2': femaleHeadModel2,
                              'resizeX': resizeX,
                              'resizeY': resizeY,
                              'resizeZ': resizeZ,
                              'colorReplace': colorReplace,
                              'colorFind': colorFind,
                              'textureReplace': textureReplace,
                              'textureFind': textureFind
                              }
                item_list.append(item_final)
            except Exception:
                pass

        item_out = open("item_defs.json", "w")
        json.dump(item_list, item_out, indent=2)
        item_out.close()

    if perform_npc:
        npc_file_list = []
        npc_path = directory + '/npc_defs/'
        print("Found ", npc_path, ", beginning dump.")
        for npc_filenames in os.walk(npc_path):
            npc_file_list.append(npc_filenames)

        npc_list = []
        for i in range(len(npc_filenames[2])):
            try:
                data = json.load(open(npc_path + npc_filenames[2][i], encoding='utf-8'))
                id = data.get('id')
                name = data.get('name')
                models = data.get('models')
                standingAnimation = data.get('standingAnimation')
                walkingAnimation = data.get('walkingAnimation')
                widthScale = data.get('widthScale')
                heightScale = data.get('heightScale')
                recolorToReplace = data.get('recolorToReplace')
                recolorToFind = data.get('recolorToFind')

                npc_final = {'id': id,
                             'name': name,
                             'models': models,
                             'standingAnimation': standingAnimation,
                             'walkingAnimation': walkingAnimation,
                             'widthScale': widthScale,
                             'heightScale': heightScale,
                             'recolorToReplace': recolorToReplace,
                             'recolorToFind': recolorToFind,
                             }
                npc_list.append(npc_final)
            except Exception:
                pass

        npc_out = open("npc_defs.json", "w")
        json.dump(npc_list, npc_out, indent=2)
        npc_out.close()


if __name__ == '__main__':
    main()
