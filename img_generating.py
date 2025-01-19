import os
import bpy
import random
import json

for i in range(1, 2):
    # importing json files (m,w,skin)
    bpy.context.scene.MPFB_FPR_available_presets = str(i)
    bpy.ops.mpfb.human_from_presets()
    
    # adding rig hellper 
    #(заранее насрой панель  rig helper, можно смому добавить через bpy.context.scene )
    bpy.ops.mpfb.add_helpers()
    
    # adding 2 random poses 
    available_poses = ['pose1', 'pose2', 'pose3', 'pose4', 'pose5', 'pose6']
    selected_poses = random.sample(available_poses, 2)
    
    for pose in selected_poses:
        bpy.context.scene.MPFB_POSES_available_poses = pose
        bpy.ops.mpfb.load_pose()
            
        # addin 2 random light sys
        availabla_lights = ['light1', 'light2', 'light3', 'light4', 'light5', 'light6', 'light7', 'light8', 'light9', 'light10'] 
        selected_lights = random.sample(availabla_lights, 2)
            
        for light_name in selected_lights:
            light_file_path = os.path.join("C:/Users/Сергей/Desktop/cmpolik/lights/", f"{light_name}.json")
                
            # Загрузка данных из JSON
            with open(light_file_path, 'r') as f:
            lights_data = json.load(f)
    
            for light_data in lights_data:
                # Создаем объект света
                light_type = light_data["type"]
                bpy.ops.object.light_add(type=light_type, location=light_data["location"])
                light_obj = bpy.context.object
        
                # Применяем свойства
                light_obj.name = light_data["name"]
                light_obj.rotation_euler = light_data["rotation"]
                light = light_obj.data
                light.energy = light_data["energy"]
                light.color = light_data["color"]
                light.shadow_soft_size = light_data["size"]  
        
                # Настройки для Point и Spot
                if light_type == "POINT" and light_data["distance"] is not None:
                    light.cutoff_distance = light_data["distance"]
                if light_type == "SPOT" and light_data["angle"] is not None:
                    light.spot_size = light_data["angle"]
    

                # addin 2 random camera sys
                availabla_cameras = ['cam1', 'cam2', 'cam3', 'cam4', 'cam5', 'cam6', 'cam7', 'cam', 'cam9', 'cam10']
                selected_cameras = random.sample(availabla_cameras, 2)
        
                for camera_name in selected_cameras:
                    cam_file_path = os.path.join("/Users/Сергей/Desktop/cmpolik/cameras/", f"{camera_name}.json")

                # Загрузка данных из JSON
                with open(cam_file_path, 'r') as file:
                    cameras_data = json.load(file)

                # Создание камер на основе данных
                for cam_data in cameras_data:
                    # Создаём объект камеры
                    camera = bpy.data.cameras.new(name=cam_data["name"])
                    camera_obj = bpy.data.objects.new(name=cam_data["name"], object_data=camera)
                    bpy.context.collection.objects.link(camera_obj)
    
                    # Устанавливаем параметры камеры
                    camera_obj.location = cam_data["location"]
                    camera_obj.rotation_euler = cam_data["rotation"]