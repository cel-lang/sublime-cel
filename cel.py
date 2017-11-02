import sublime
import sublime_plugin

class EventDump(sublime_plugin.EventListener):
    TIMEOUT_MS = 100
    def __init__(self):
        self.pending = 0

    def on_modified(self, view):
        if not self.settings.get("live_parser"):
            return
        filename = view.file_name()
        if not filename or not filename.endswith('.cel'):
            return
        self.pending = self.pending + 1
        sublime.set_timeout(lambda: self.parse(view), self.TIMEOUT_MS)
            
    def on_pre_save_async(self, view):
        filename = view.file_name()
        if not filename or not filename.endswith('.cel'):
            return
        print( "Run celfmt" )
        print (view.file_name(), view.is_primary(), "just got saved")

        #set_syntax_file
    def on_activated_async(self, view):
        self.settings = sublime.load_settings("Cel.sublime-settings")
        
        filename = view.file_name()
        if not filename or not filename.endswith('.cel'):
            return
        print( "Run celfmt" )
        
        view.run_command("example")  # None    Runs the named TextCommand with the (optional) given args.
#    def parse(self, view):
#        # Don't bother parsing if there's another parse command pending
#        self.pending = self.pending - 1
#        if self.pending > 0:
#            return
#        # Grab the path to luac from the settings
#        luac_path = self.settings.get("luac_path")
#        # Run luac with the parse option
#        p = Popen(luac_path + ' -p -', stdin=PIPE, stderr=PIPE, shell=True)
#        text = view.substr(sublime.Region(0, view.size()))
#        errors = p.communicate(text.encode('utf-8'))[1]
#        result = p.wait()
#        # Clear out any old region markers
#        view.erase_regions('lua')
#        # Nothing to do if it parsed successfully
#        if result == 0:
#            return
#        # Add regions and place the error message in the status bar
#        errors = errors.decode("utf-8")
#        sublime.status_message(errors)
#        pattern = re.compile(r':([0-9]+):')
#        regions = [view.full_line(view.text_point(int(match) - 1, 0)) for match in pattern.findall(errors)]
#        view.add_regions('lua', regions, 'invalid', 'DOT', sublime.HIDDEN)

class ExampleCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        print("Example" )
