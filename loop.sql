-- select * from play_time;
--create table play_time_copy as select * from play_time; 
--delete from play_time_copy;
-- select * from play_time_copy;
DO $$
DECLARE
    p_time_id   play_time_copy.play_time_id%TYPE;
    p_time play_time_copy.play_time%TYPE;

BEGIN
    p_time_id := 0;
    p_time := 1;
    FOR counter IN 1..10
        LOOP
            INSERT INTO play_time_copy(play_time_id, play_time)
            VALUES (counter + p_time_id, p_time + 5*counter);
        END LOOP;
END;
$$