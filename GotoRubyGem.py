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
    # TODO: This version only supports Linux and RVM as Ruby manager.

    # Get the current Ruby version
    ruby_version = os.popen("rvm current").read().split("\n")[0]

    rvm_gems_directories = [
      os.path.expanduser("~/.rvm/gems/%s/gems/" % ruby_version),
      os.path.expanduser("~/.rvm/gems/%s/bundler/gems/" % ruby_version)
    ]

    # Create a list to store gem names and their absolute paths
    gems_list = []

    for gems_directory in rvm_gems_directories:

      # List all files and directories in the gems directory
      gems = os.listdir(gems_directory)

      # Iterate over the gems and their absolute paths
      for gem in gems:
          gem_path = os.path.join(gems_directory, gem)
          gems_list.append((gem, gem_path))

    return gems_list
