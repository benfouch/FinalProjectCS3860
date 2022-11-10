DROP Table If EXISTS non_actors;
CREATE TABLE non_actors 
AS 
SELECT
	v.recording_id,
	v.name
FROM video_actors v;

DROP Table If EXISTS non_video_info;
CREATE TABLE non_video_info
AS
SELECT 
	v.*, 
	s.price, 
	s.stock_count
FROM my_video_recordings v, video_actors a, my_stock_info s
WHERE v.recording_id = a.recording_id
AND v.recording_id = s.recording_id;

