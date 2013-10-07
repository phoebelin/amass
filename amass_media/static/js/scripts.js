$(document).ready(function() {
    $('.datepicker-default').datepicker({
	format:'yyyy-mm-dd'
    });

    $('.timepicker-default').timepicker({
	minuteStep: 1,
	showSeconds: true,
	showMeridian: false
    });
})
