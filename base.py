import os
import shutil

class Base(object):
    def init(self, **kwargs):
        pass
    def build(self, **kwargs):
        pass
    def publish(self, **kwargs):
        pass

    def newer_file(self, src_path, dst_path):
        if not os.path.isfile(dst_path) or \
            (os.path.getmtime(src_path) > os.path.getmtime(dst_path)):
                return true
        return false

    def copy_newer_files(self, **kwargs):
        src_path = os.path.join(kwargs['src_dir'], fname)
        dst_path = os.path.join(kwargs['dst_dir'], fname)
        for fname in kwargs['file_names']:
            if self.newer_file(src_path, dst_path):
                print('copy ' + src_path + ' to ' + dst_path)
                shutil.copy2(src_path, dst_path)

    def markdown_newer_files(self, **kwargs):
        src_path = os.path.join('.', fname)
        dst_path = os.path.join(kwargs['dst_dir'], fname)
        for fname in kwargs['file_names']:
            if self.newer_file(src_path, dst_path):
                print('markdown ' + src_path + ' to ' + dst_path)
            
    def mustache_newer_files(self, **kwargs):
        src_path = os.path.join('.', fname)
        dst_path = os.path.join(kwargs['dst_dir'], fname)
        for fname in kw_args['file_names']:
            if self.newer_file(src_path, dst_path):
                print('mustache ' + src_path + ' to ' + dst_path)
