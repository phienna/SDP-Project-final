class Hardware:

    def get_cpu_temp(self):
        import os

        temp = os.popen("vcgencmd measure_temp").readline()
        return temp

    def get_config_int(self):
        import os

        config_int = os.popen("vcgencmd get_config int").read()
        return config_int

    def get_disk_usage(self):
        import os

        usage = os.popen("df -h").read()
        return usage

# print(get_cpu_temp())
