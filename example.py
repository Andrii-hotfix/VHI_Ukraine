from spyre import server

class SimpleApp(server.App):
    title = "Simple App"
    inputs = [dict( type='text',
                    key='words',
                    label='write words here',
                    value='hello word',
                    action_id='simple_html_output')]

    outputs = [dict( type='html',
                     id='simple_html_output' )]
                     
    def getHTML(self, params):
        words = params["words"]
        return "Here's what you wrote in the textbox: <br>%s<br>" % words

app = SimpleApp()
app.launch()
