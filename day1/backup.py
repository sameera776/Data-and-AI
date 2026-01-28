import shutil
import datetime
source="C:/Users/vemul/OneDrive/Desktop/Data and AI/data.txt" 
backup=f"C:/Users/vemul/OneDrive/Desktop/Data and AI/data_backup_{datetime.date.today()}.txt"
shutil.copy(source,backup)
print(f"Backup of {source} created at {backup}")