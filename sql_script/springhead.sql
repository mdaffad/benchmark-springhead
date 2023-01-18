select sum(time_ns) from springhead_times WHERE type_timer='get_handler';
select COUNT(*) from springhead_times WHERE type_timer='get_handler';
select sum(time_ns) from springhead_times WHERE type_timer='bootstrap';
select COUNT(*) from springhead_times WHERE type_timer='bootstrap';
select sum(time_ns) from springhead_times WHERE type_timer='endpoint';
select COUNT(*) from springhead_times WHERE type_timer='endpoint';