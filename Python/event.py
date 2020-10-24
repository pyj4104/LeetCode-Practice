Event CreateEvent(int eventId, Date startDate, int eventDurationInDays) {

    Event event = new Event();

    event.eventId = eventId;

    int startDayOfWeek = GetDayOfWeek(startDate);

    int endDayOfWeek =

    event.startDayOfWeek = startDayOfWeek;

    event.endDayOfWeek = endDayOfWeek;

    assert(0 <= event.startDayOfWeek && event.startDayOfWeek < 7);

    assert(0 <= event.endDayOfWeek && event.endDayOfWeek < 7);

    return event;

}