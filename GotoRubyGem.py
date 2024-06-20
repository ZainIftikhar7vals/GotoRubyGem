import sublime
import sublime_plugin
import os

SETTINGS_FILE = "GotoRubyGem.sublime-settings"

class GotoRubyGemCommand(sublime_plugin.WindowCommand):
  def run(self, gem):
    # If Gems directories are empty then early return.
    if not gem:
      return

    sublime.run_command('new_window')
    new_window = sublime.active_window()
    project_data = { "folders": [{"path": gem}] }
    new_window.set_project_data(project_data)

  def input(self, args):
    return GemInputHandler()

class GemInputHandler(sublime_plugin.ListInputHandler):

  def list_items(self):
    settings = sublime.load_settings(SETTINGS_FILE)
    use_custom_gems_directories = settings.get("use_custom_gems_directories", False)

    if use_custom_gems_directories:
      gems_directories = settings.get("custom_gems_directories", [])
    else:
      gem_home = os.environ["GEM_HOME"]
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
