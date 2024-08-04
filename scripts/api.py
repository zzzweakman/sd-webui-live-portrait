from fastapi import FastAPI
import gradio as gr

from liveportrait.config.argument_config import ArgumentConfig
from liveportrait.config.crop_config import CropConfig
from liveportrait.config.inference_config import InferenceConfig
from liveportrait.live_portrait_pipeline import LivePortraitPipeline
from liveportrait.live_portrait_pipeline_animal import LivePortraitPipelineAnimal
from liveportrait.config.base_config import make_abs_path


def live_portrait_api(_: gr.Blocks, app: FastAPI):
    @app.post("/live-portrait/video")
    async def execute_video() -> str:
        print("Live Portrait API /live-portrait/video received request")
        live_portrait_pipeline = LivePortraitPipeline(
            inference_cfg=InferenceConfig(),
            crop_cfg=CropConfig()
        )

        source = make_abs_path('../../assets/examples/source/s0.jpg')
        driving = make_abs_path('../../assets/examples/driving/d0.mp4')

        live_portrait_pipeline.execute(ArgumentConfig(
            source=source,
            driving=driving
        ))
        
        print("Live Portrait API /live-portrait/video finished")
        return "OK"
    
    @app.post("/live-portrait/animal/video")
    async def execute_animal_video() -> str:
        print("Live Portrait API /live-portrait/animal/video received request")
        live_portrait_pipeline_animal = LivePortraitPipelineAnimal(
            inference_cfg=InferenceConfig(),
            crop_cfg=CropConfig()
        )

        source = make_abs_path('../../assets/examples/source/s39.jpg')
        driving = make_abs_path('../../assets/examples/driving/wink.pkl')

        live_portrait_pipeline_animal.execute(ArgumentConfig(
            source=source,
            driving=driving,
            driving_multiplier=1.75,
            flag_stitching=False
        ))
        
        print("Live Portrait API /live-portrait/animal/video finished")
        return "OK"


try:
    import modules.script_callbacks as script_callbacks
    script_callbacks.on_app_started(live_portrait_api)
except:
    print("Live Portrait API failed to initialize")