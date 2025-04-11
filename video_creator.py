from moviepy.editor import ImageClip, TextClip, CompositeVideoClip, AudioFileClip
import os

def create_video(image_path, audio_path, output_path, text=None, duration=5):
    clips = []

    # Check and set image path
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"❌ Image not found at {image_path}")

    # Load Image Clip
    image_clip = ImageClip(image_path).set_duration(duration)
    clips.append(image_clip)

    # Add Text Clip if text is provided
    if text:
        txt_clip = TextClip(
            text, fontsize=40, color='white', font='Arial-Bold', size=image_clip.size, method='caption'
        )
        txt_clip = txt_clip.set_position('center').set_duration(duration)
        clips.append(txt_clip)

    # Create Composite Clip
    final = CompositeVideoClip(clips)

    # Add Audio if provided
    if audio_path:
        if not os.path.exists(audio_path):
            raise FileNotFoundError(f"❌ Audio not found at {audio_path}")
        audio = AudioFileClip(audio_path).set_duration(final.duration)
        final = final.set_audio(audio)

    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Export Final Video
    final.write_videofile(output_path, fps=24)

    return output_path


# Optional: Standalone test
if __name__ == "__main__":
    create_video(
        image_path="assets/sample.jpg",
        audio_path="assets/voice.mp3",
        output_path="output/final_video.mp4",
        text="Welcome to EduGenAI!",
        duration=5
    )
