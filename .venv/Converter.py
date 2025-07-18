import json
import os.path
import threading
import re
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
    perform_anim = True

    # 0 8057, stand
    # 1 819, walk
    # 2 824, run
    # 3 820, walk backwards
    # 4 821, shuffle left
    # 5 822, shuffle right
    # 6 823, rotate
    # 7 -1, stab
    # 8 8056, slash
    # 9 8056, crush
    # 10 -1, spec
    # 11 -1, defend
    # 12 -1, slash2
    # 13 -1 crush2

    t1 = threading.Thread(target=obj, args=(directory, perform_obj,))
    t2 = threading.Thread(target=npc, args=(directory, perform_npc,))
    t3 = threading.Thread(target=item, args=(directory, perform_item,))
    t4 = threading.Thread(target=anim, args=(directory, perform_anim,))

    t1.start()
    t2.start()
    t3.start()
    t4.start()

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
        print("Finished kit")

    if perform_spotanim:
        spotanim_file_list = []
        spotanim_path = directory + '/spotanims/'
        print("Found ", spotanim_path, ", beginning dump.")
        for spotanim_filenames in os.walk(spotanim_path):
            spotanim_file_list.append(spotanim_filenames)

        naming_data = json.load((open("C:/Users/Matheus/PycharmProjects/cache-converter/.venv/spotanims.json", encoding='utf-8')))

        spotanim_list = []
        for i in range(len(spotanim_filenames[2])):
            try:
                data = json.load(open(spotanim_path + spotanim_filenames[2][i], encoding='utf-8'))

                id = data.get('id')
                name = 'Unnamed'

                for sa in naming_data:
                    if sa.get('id') == id:
                        name = sa.get('name')
                        break

                #name = data.get('debugName')
                #name = name.replace('_', ' ')
                #name = name.capitalize()

                modelId = data.get('modelId')
                animationId = data.get('animationId')
                resizeX = data.get('resizeX')
                resizeY = data.get('resizeY')
                ambient = data.get('ambient')
                contrast = data.get('contrast')
                recolorToReplace = data.get('recolorToReplace')
                recolorToFind = data.get('recolorToFind')
                spotanim_final = {'name': name,
                                  'id': id,
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

        json_file = json.dumps(spotanim_list)
        data = json.loads(json_file)
        sorted_file = sorted(data, key=lambda x: x['id'])
        json.dump(sorted_file, spotanim_out, indent=2, sort_keys=False)

        spotanim_out.close()
        print("Finished spotanim")

    if perform_seq:
        seq_file_list = []
        seq_path = directory + '/sequences/'
        print("Found ", seq_path, ", beginning dump.")
        for seq_filenames in os.walk(seq_path):
            seq_file_list.append(seq_filenames)

        naming_data = json.load((open("C:/Users/Matheus/PycharmProjects/cache-converter/.venv/sequences.json", encoding='utf-8')))

        seq_list = []
        for i in range(len(seq_filenames[2])):
            try:
                data = json.load(open(seq_path + seq_filenames[2][i], encoding='utf-8'))

                id = data.get('id')
                name = 'Unnamed'

                for sa in naming_data:
                    if sa.get('id') == id:
                        name = sa.get('name')
                        break

                #name = data.get('debugName')
                #name = name.replace('_', ' ')
                #name = name.capitalize()

                leftHandItem = data.get('leftHandItem')
                rightHandItem = data.get('rightHandItem')
                seq_final = {
                    'name': name,
                    'id': id,
                    'rightHandItem': rightHandItem,
                    'leftHandItem': leftHandItem
                }
                seq_list.append(seq_final)
            except Exception:
                pass

        seq_out = open("sequences.json", "w")

        json_file = json.dumps(seq_list)
        data = json.loads(json_file)
        sorted_file = sorted(data, key=lambda x: x['id'])
        json.dump(sorted_file, seq_out, indent=2)

        seq_out.close()
        print("Finished seq")

        t1.join()
        t2.join()
        t3.join()
        t4.join()
        print("Finishing program")


def obj(directory, perform_obj):
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

                if name.startswith('<'):
                    name = re.sub('<col=.{6}>', '', name)
                    name = name.replace('</col>', '')

                animationId = data.get('animationID')
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
                             'animationId': animationId,
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
        print("Finished obj")


def item(directory, perform_item):
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

                if name == "null" or name == "Null":
                    continue

                inventoryModel = data.get('inventoryModel')
                maleModel0 = data.get('maleModel0')
                maleModel1 = data.get('maleModel1')
                maleModel2 = data.get('maleModel2')
                maleOffset = data.get('maleOffset')
                femaleModel0 = data.get('femaleModel0')
                femaleModel1 = data.get('femaleModel1')
                femaleModel2 = data.get('femaleModel2')
                femaleOffset = data.get('femaleOffset')
                wearPos0 = data.get('wearPos1')
                wearPos1 = data.get('wearPos2')
                wearPos2 = data.get('wearPos3')
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
                              'wearPos0': wearPos0,
                              'wearPos1': wearPos1,
                              'wearPos2': wearPos2,
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
        print("Finished item")


def npc(directory, perform_npc):
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

                if name == 'null' or name == '' or name == '? ? ? ?':
                    continue

                if name.startswith('<'):
                    name = re.sub('<col=.{6}>', '', name)
                    name = name.replace('</col>', '')

                if name.startswith(' '):
                    name = name.replace(' ', '', 1)

                models = data.get('models')
                size = data.get('size')
                standingAnimation = data.get('standingAnimation')
                walkingAnimation = data.get('walkingAnimation')
                runAnimation = data.get('runAnimation')
                idleRotateLeftAnimation = data.get('idleRotateLeftAnimation')
                idleRotateRightAnimation = data.get('idleRotateRightAnimation')
                rotate180Animation = data.get('rotate180Animation')
                rotateLeftAnimation = data.get('rotateLeftAnimation')
                rotateRightAnimation = data.get('rotateRightAnimation')
                widthScale = data.get('widthScale')
                heightScale = data.get('heightScale')
                recolorToReplace = data.get('recolorToReplace')
                recolorToFind = data.get('recolorToFind')

                npc_final = {'id': id,
                             'name': name,
                             'models': models,
                             'size': size,
                             'standingAnimation': standingAnimation,
                             'walkingAnimation': walkingAnimation,
                             'runAnimation': runAnimation,
                             'idleRotateLeftAnimation': idleRotateLeftAnimation,
                             'idleRotateRightAnimation': idleRotateRightAnimation,
                             'rotate180Animation': rotate180Animation,
                             'rotateLeftAnimation': rotateLeftAnimation,
                             'rotateRightAnimation': rotateRightAnimation,
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
        print("Finished npc")


def anim(directory, perform_anim):
    if perform_anim:
        anim_file_list = []
        anim_path = directory + '/gamevals/7/'
        print("Found ", anim_path, ", beginning dump.")
        for anim_filenames in os.walk(anim_path):
            anim_file_list.append(anim_filenames)

        anim_list = []
        for i in range(len(anim_filenames[2])):
            try:
                data = json.load(open(anim_path + anim_filenames[2][i], encoding='utf-8'))
                id = data.get('id')
                name = data.get('name')
                name = name.replace('_', ' ')
                name = name.capitalize()

                anim_final = {'id': id,
                              'name': name
                              }
                anim_list.append(anim_final)
            except Exception:
                pass

        anim_out = open("anims.json", "w")

        json_file = json.dumps(anim_list)
        data = json.loads(json_file)
        sorted_file = sorted(data, key=lambda x: x['id'])
        json.dump(sorted_file, anim_out, indent=2)

        anim_out.close()
        print("Finished anim")


if __name__ == '__main__':
    main()
