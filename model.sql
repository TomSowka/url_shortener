BEGIN;
--
-- Create model URL
--
CREATE TABLE "url_shortener_url" 
(
"url_id" varchar(6) NOT NULL PRIMARY KEY, 
"long_url" varchar(200) NOT NULL, 
"created" datetime NOT NULL, 
"visited" integer NOT NULL
);

COMMIT;
