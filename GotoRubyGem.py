import sublime
import sublime_plugin
import os

class GotoRubyGemCommand(sublime_plugin.WindowCommand):
  def run(self, gem):
    sublime.run_command('new_window')
    new_window = sublime.active_window()
    project_data = { "folders": [{"path": gem}] }
    new_window.set_project_data(project_data)

  def input(self, args):
    return GemInputHandler()

class GemInputHandler(sublime_plugin.ListInputHandler):

  def list_items(self):
    gem_home = os.popen("echo $GEM_HOME").read().split("\n")[0]

    gems_directories = [
      os.path.expanduser("%s/gems/" % gem_home),
      os.path.expanduser("%s/bundler/gems/" % gem_home)
    ]

    # Create a list to store gem names and their absolute paths
    gems_list = []

    for gems_directory in gems_directories:
      # List all Gems
      gems = os.listdir(gems_directory)

      for gem in gems:
          gem_path = os.path.join(gems_directory, gem)
          gems_list.append((gem, gem_path))

    return gems_list
