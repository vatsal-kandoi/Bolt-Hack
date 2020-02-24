from recorder import Recorder
import time

rec = Recorder(channels=2) 
print(rec.get_device_info())  
recfile = self.rec.open('a.wav', 'wb')    
recfile.start_recording();
time.sleep(2);
recfile.stop_recording();
recfile.close();