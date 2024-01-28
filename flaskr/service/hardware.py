class Hardware:

    def get_cpu_temp(self):
        import os

        temp = os.popen("vcgencmd measure_temp").readline()
        return temp
    
    def get_disk_usage(self):
        import os
        temp = os.popen("df -h").readline()
        return temp

# print(get_cpu_temp())
