import os
import subprocess
InputFileName = "InputFile\\video.mp4"
OutPutFileName = "OutPutFile\\video.mp4"
OutPutFileName2 = "OutPutFile2\\video.mp4"
class ffmpeg_module: #class created for running transcoding operations
    def copy_file(self): #copy exact file from input file location to output file location
        command = f"ffmpeg -i {InputFileName} {OutPutFileName}"
        subprocess.run(command)

    def trimming(self, startduration, endduration): #trim function
        command = f"ffmpeg -ss [{startduration}] -i {OutPutFileName} -t [{endduration}] {OutPutFileName2}"
        subprocess.run(command)
        os.replace(OutPutFileName2, OutPutFileName)
        os.remove(OutPutFileName2)

    def change_aspect_ratio(self, aspectratio): #change aspect ratio function
        command = f"ffmpeg -i {OutPutFileName} -aspect[{aspectratio}] {OutPutFileName2}"
        subprocess.run(command)
        os.replace(OutPutFileName2, OutPutFileName)
        os.remove(OutPutFileName2)

    def change_bitrate(self, BitRateValue): #change bitrate function
        command = f"ffmpeg -i {OutPutFileName} -b:v {BitRateValue} {OutPutFileName2}"
        subprocess.run(command)
        os.replace(OutPutFileName2, OutPutFileName)
        os.remove(OutPutFileName2)

    def change_frame_rate(self, framerate): #change frame rate function
        command = f"ffmpeg -i {OutPutFileName} -r {framerate}  {OutPutFileName2}"
        subprocess.run(command)
        os.replace(OutPutFileName2, OutPutFileName)
        os.remove(OutPutFileName2)

    def change_frame_size(self, framesize): #change frame size function
        command = f"ffmpeg -i {OutPutFileName} -s {framesize}  {OutPutFileName2}"
        subprocess.run(command)
        os.replace(OutPutFileName2, OutPutFileName)
        os.remove(OutPutFileName2)

    def mute_audio(self): #mute audio function
        command = f"ffmpeg -i {OutPutFileName} -map_channel -1 -map_channel 0.0.1 {OutPutFileName2}"
        subprocess.run(command)
        os.replace(OutPutFileName2, OutPutFileName)
        os.remove(OutPutFileName2)

    def remove_video(self): #remove video function
        command = f"ffmpeg.exe -i {OutPutFileName} -c:v copy -an {OutPutFileName2}"
        subprocess.run(command)
        os.replace(OutPutFileName2, OutPutFileName)
        os.remove(OutPutFileName2)

    def convert_hls(self): #convert the video to hls
        #Get filename without extension
        StripOut = OutPutFileName.split(".")
        OutPutFileName2 = f"{StripOut}.m3u8"
        command = f"ffmpeg -i {OutPutFileName}  -codec: copy -start_number 0 -hls_time 10 -hls_list_size 0 -f hls {OutPutFileName2}"
        subprocess.run(command)
        os.replace(OutPutFileName2, OutPutFileName)
        os.remove(OutPutFileName2)





