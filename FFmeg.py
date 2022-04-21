import os
import subprocess
InputFileName = ""
OutPutFileName = ""
OutPutFileName2 = ""
class ffmpeg_module:
    def copy_file(self):
        command = f"ffmpeg -i {InputFileName} {OutPutFileName}"
        subprocess.run(command)

    def trimming(self, startduration, endduration):
        command = f"ffmpeg -ss [{startduration}] -i {OutPutFileName} -t [{endduration}] {OutPutFileName2}"
        subprocess.run(command)
        os.replace(OutPutFileName2, OutPutFileName)
        os.remove(OutPutFileName2)

    def change_aspect_ratio(self, aspectratio):
        command = f"ffmpeg -i {OutPutFileName} -aspect[{aspectratio}] {OutPutFileName2}"
        subprocess.run(command)
        os.replace(OutPutFileName2, OutPutFileName)
        os.remove(OutPutFileName2)

    def change_bitrate(self, BitRateValue):
        command = f"ffmpeg -i {OutPutFileName} -b:v {BitRateValue} {OutPutFileName2}"
        subprocess.run(command)
        os.replace(OutPutFileName2, OutPutFileName)
        os.remove(OutPutFileName2)

    def change_frame_rate(self, framerate):
        command = f"ffmpeg -i {OutPutFileName} -r {framerate}  {OutPutFileName2}"
        subprocess.run(command)
        os.replace(OutPutFileName2, OutPutFileName)
        os.remove(OutPutFileName2)

    def change_frame_size(self, framesize):
        command = f"ffmpeg -i {OutPutFileName} -s {framesize}  {OutPutFileName2}"
        subprocess.run(command)
        os.replace(OutPutFileName2, OutPutFileName)
        os.remove(OutPutFileName2)

    def mute_audio(self):
        command = f"ffmpeg -i {OutPutFileName} -map_channel -1 -map_channel 0.0.1 {OutPutFileName2}"
        subprocess.run(command)
        os.replace(OutPutFileName2, OutPutFileName)
        os.remove(OutPutFileName2)

    def remove_video(self):
        command = f"ffmpeg.exe -i {OutPutFileName} -c:v copy -an {OutPutFileName2}"
        subprocess.run(command)
        os.replace(OutPutFileName2, OutPutFileName)
        os.remove(OutPutFileName2)

    def convert_hls(self):
        #Get filename without extension
        StripOut = OutPutFileName.split(".")
        OutPutFileName2 = f"{StripOut}.m3u8"
        command = f"ffmpeg -i {OutPutFileName}  -codec: copy -start_number 0 -hls_time 10 -hls_list_size 0 -f hls {OutPutFileName2}"
        subprocess.run(command)
        os.replace(OutPutFileName2, OutPutFileName)
        os.remove(OutPutFileName2)





