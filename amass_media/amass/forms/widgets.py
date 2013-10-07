from django.forms.widgets import Input
from django.utils.safestring import mark_safe
from django.forms.widgets import MultiWidget, DateInput, TimeInput

from time import strftime

class DatePickerWidget(DateInput):

    def render(self, name, value, attrs=None):
        attrs = {'class': 'datepicker-default input-datepicker'}
        append_text = self.attrs.get('text', '<i class="icon-calendar"></i>')
        return mark_safe(u'<div style="display:inline" class="input-append">%s<span class="add-on">%s</span></div>' % (super(DatePickerWidget, self).render(name, value, attrs), append_text))

class TimePickerWidget(TimeInput):

    def render(self, name, value, attrs=None):
        attrs = {'class': 'timepicker-default input-timepicker'}
        append_text = self.attrs.get('text', '<i class="icon-time"></i>')
        return mark_safe(u'<div style="display:inline" class="input-append bootstrap-timepicker">%s<span class="add-on">%s</span></div>' % (super(TimePickerWidget, self).render(name, value, attrs), append_text))
        #return mark_safe(u'<div style="display:inline" class="bootstrap-timepicker">%s</div>' % (super(TimePickerWidget, self).render(name, value, attrs)))

class BootstrapSplitDateTimeWidget(MultiWidget):

    def __init__(self, attrs=None, date_format=None, time_format=None):
        date_class = attrs['date_class']
        time_class = attrs['time_class']
        del attrs['date_class']
        del attrs['time_class']

        time_attrs = attrs.copy()
        time_attrs['class'] = time_class

        date_attrs = attrs.copy()
        date_attrs['class'] = date_class

        widgets = (DatePickerWidget(attrs=date_attrs, format=date_format), TimePickerWidget(attrs=time_attrs, format=time_format))

        super(BootstrapSplitDateTimeWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            d = strftime("%Y-%m-%d", value.timetuple())
            hour = strftime("%H", value.timetuple())
            minute = strftime("%M", value.timetuple())
            meridian = strftime("%p", value.timetuple())
            return (d, hour+":"+minute, meridian)
        else:
            return (None, None, None)

    def format_output(self, rendered_widgets):
        """
        Given a list of rendered widgets (as strings), it inserts an HTML
        linebreak between them.

        Returns a Unicode string representing the HTML for the whole lot.
        """
        return "Date: %s<br/>Time: %s" % (rendered_widgets[0], rendered_widgets[1])


