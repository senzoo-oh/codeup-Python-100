w, h, b = map(int, input().split())

memory_needed = w * h * b
memory_needed_in_MB = (((memory_needed/8)/1024)/1024)

print("%.2f MB" % memory_needed_in_MB)