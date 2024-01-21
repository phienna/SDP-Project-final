class Hardware:

    def get_cpu_temp(self):
        import os

        temp = os.popen("vcgencmd measure_temp").readline()
        return temp

# print(get_cpu_temp())
