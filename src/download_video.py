from pytube import YouTube
import moviepy.editor as mp


class DownloadVideos:
    def dowloadVideo(self,urlVideo):
        yt = YouTube(url=urlVideo)
        res = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(
            output_path='files/')
        return res

    
    def convert(self,path):
       clip = mp.VideoFileClip(r'{}'.format(path))
       clip.audio.write_audiofile('{}mp3'.format(path[:-3]))
       newPath = '{}mp3'.format(path[:-3])
       return newPath
       
       