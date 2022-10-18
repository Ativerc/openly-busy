import pulsectl

with pulsectl.Pulse('event-printer') as pulse:
	print('Event types:', pulsectl.PulseEventTypeEnum)
	print('Event facilitites:', pulsectl.PulseEventFacilityEnum)
	print('Event masks:', pulsectl.PulseEventMaskEnum)

	def print_events(ev):
		print('Pulse event: ', ev)
		### Raise PulseLoopStop for event_listen() to return before timeout (if any)
    		# raise pulsectl.PulseLoopStop

	pulse.event_mask_set('all')
	pulse.event_callback_set(print_events)
	pulse.event_listen(timeout=10)
