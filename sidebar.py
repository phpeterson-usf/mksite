from base import Base

class Sidebar(Base):
    def init(self, **kwargs):
        kwargs['file_names'] = ['sidebar.md', 'sidebar.css', 'logo.png']
        self.copy_newer_files(**kwargs)

    def build(self, **kwargs):
        kwargs['file_names'] = ['sidebar.md']
        self.markdown_newer_files(kwargs)

    def publish(self, **kwargs):
        pass
