import sublime, sublime_plugin, os, subprocess, datetime, shutil
 
class CreateBackupCopy(sublime_plugin.TextCommand):
    def run(self, edit):
        if self.view.file_name():
            file_name = self.view.file_name()
            dir_name = os.path.dirname(file_name)
            base_name = os.path.basename(file_name)
            base_base, base_ext = os.path.splitext(base_name)
            time_stamp = datetime.datetime.now().strftime(" [%H][%M][%S]")
            target_dir = os.path.join(dir_name, '.sublime-backup')
            target_file = base_base+time_stamp+base_ext
            target_target = os.path.join(target_dir, target_file)
			
            os.makedirs(target_dir, exist_ok=True)
			
            date_dir = os.path.join(target_dir, datetime.datetime.now().strftime("Data [%Y][%m][%d]"))
            os.makedirs(date_dir, exist_ok=True)
			
            file_dir = os.path.join(date_dir, base_base)
            os.makedirs(file_dir, exist_ok=True)
			

            target_target = os.path.join(file_dir, target_file)
            try:
                shutil.copyfile(file_name, target_target)
                sublime.status_message("Created backup copy %s" % target_file)
            except:
                sublime.status_message("Error while copying file")
