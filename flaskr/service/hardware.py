class Hardware:

    def get_cpu_temp(self):
        import os

        temp = os.popen("vcgencmd measure_temp").readline()
        return temp
    
    def get_config_int(self):
        import os

        config_int = os.popen("vcgencmd get_config int").readline()
        return config_int

# print(get_cpu_temp())
