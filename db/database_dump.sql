--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: images; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE images (
    id integer NOT NULL,
    main_id integer NOT NULL,
    name character varying(100),
    path character varying(250),
    alt character varying(200)
);


ALTER TABLE public.images OWNER TO postgres;

--
-- Name: images_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE images_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.images_id_seq OWNER TO postgres;

--
-- Name: images_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE images_id_seq OWNED BY images.id;


--
-- Name: images_main_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE images_main_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.images_main_id_seq OWNER TO postgres;

--
-- Name: images_main_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE images_main_id_seq OWNED BY images.main_id;


--
-- Name: listing_provider; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE listing_provider (
    id integer NOT NULL,
    main_id integer NOT NULL,
    listing_agent character varying(100),
    agent_phone_number character varying(25),
    listed_by character varying(100),
    broker_location character varying(50),
    data_source character varying(50)
);


ALTER TABLE public.listing_provider OWNER TO postgres;

--
-- Name: listing_provider_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE listing_provider_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.listing_provider_id_seq OWNER TO postgres;

--
-- Name: listing_provider_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE listing_provider_id_seq OWNED BY listing_provider.id;


--
-- Name: listing_provider_main_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE listing_provider_main_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.listing_provider_main_id_seq OWNER TO postgres;

--
-- Name: listing_provider_main_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE listing_provider_main_id_seq OWNED BY listing_provider.main_id;


--
-- Name: main; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE main (
    id integer NOT NULL,
    address text,
    city text,
    state character varying(2),
    zip_code character varying(10),
    bedrooms smallint,
    bathrooms_full smallint,
    bathrooms_half smallint,
    square_feet character varying(20),
    square_feet_lot character varying(20),
    price character varying(20),
    description text,
    style character varying(250),
    home_type character varying(250),
    year_built character varying(4),
    price_per_square_foot character varying(20),
    date_posted timestamp without time zone,
    status character varying(20),
    longitude character varying(20),
    latitude character varying(20),
    create_date timestamp without time zone,
    original_url text,
    features json
);


ALTER TABLE public.main OWNER TO postgres;

--
-- Name: main_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE main_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.main_id_seq OWNER TO postgres;

--
-- Name: main_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE main_id_seq OWNED BY main.id;


--
-- Name: schools; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE schools (
    id integer NOT NULL,
    main_id integer NOT NULL,
    score character varying(10),
    name character varying(100),
    grades character varying(10),
    distance character varying(10)
);


ALTER TABLE public.schools OWNER TO postgres;

--
-- Name: schools_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE schools_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.schools_id_seq OWNER TO postgres;

--
-- Name: schools_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE schools_id_seq OWNED BY schools.id;


--
-- Name: schools_main_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE schools_main_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.schools_main_id_seq OWNER TO postgres;

--
-- Name: schools_main_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE schools_main_id_seq OWNED BY schools.main_id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY images ALTER COLUMN id SET DEFAULT nextval('images_id_seq'::regclass);


--
-- Name: main_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY images ALTER COLUMN main_id SET DEFAULT nextval('images_main_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY listing_provider ALTER COLUMN id SET DEFAULT nextval('listing_provider_id_seq'::regclass);


--
-- Name: main_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY listing_provider ALTER COLUMN main_id SET DEFAULT nextval('listing_provider_main_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY main ALTER COLUMN id SET DEFAULT nextval('main_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY schools ALTER COLUMN id SET DEFAULT nextval('schools_id_seq'::regclass);


--
-- Name: main_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY schools ALTER COLUMN main_id SET DEFAULT nextval('schools_main_id_seq'::regclass);


--
-- Data for Name: images; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY images (id, main_id, name, path, alt) FROM stdin;
1	1	l895ab545-m0xd-w640_h480_q80.jpg	images/l895ab545-m0xd-w640_h480_q80.jpg	1000 1st Ave Unit 2301, Seattle, WA 98104
2	1	l895ab545-m1xd-w640_h480_q80.jpg	images/l895ab545-m1xd-w640_h480_q80.jpg	1000 1st Ave Unit 2301, Seattle, WA 98104
3	1	l895ab545-m2xd-w640_h480_q80.jpg	images/l895ab545-m2xd-w640_h480_q80.jpg	1000 1st Ave Unit 2301, Seattle, WA 98104
\.


--
-- Name: images_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('images_id_seq', 3, true);


--
-- Name: images_main_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('images_main_id_seq', 1, false);


--
-- Data for Name: listing_provider; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY listing_provider (id, main_id, listing_agent, agent_phone_number, listed_by, broker_location, data_source) FROM stdin;
1	1	Erica Clibborn	(206) 527-5445	Windermere Real Estate Midtown	\N	Seattle
\.


--
-- Name: listing_provider_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('listing_provider_id_seq', 1, true);


--
-- Name: listing_provider_main_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('listing_provider_main_id_seq', 1, false);


--
-- Data for Name: main; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY main (id, address, city, state, zip_code, bedrooms, bathrooms_full, bathrooms_half, square_feet, square_feet_lot, price, description, style, home_type, year_built, price_per_square_foot, date_posted, status, longitude, latitude, create_date, original_url, features) FROM stdin;
1	1000 1st Ave Unit 2301	Seattle	WA	98104	2	2	1	1,769	\N	2,300,000	Magnificent sweeping views of the city, Elliott Bay and mountains high atop Madison Tower. Over 1,700 sq ft of light-filled living spaces punctuated with glamourous accents; chic wallpapers, elegant lighting, Lumicor doors and a chef-worthy kitchen featuring SubZero refrigerator, Wolf Range and granite countertops. The luxurious master suite boasts city views and an impressive ensuite bath + dressing room. Residents enjoy Hotel 1000s five-star luxury amenties. 2-car parking	\N	Condo/townhome/row home/co-op	2006	1,300	2016-03-17 00:00:00	Active	-122.336106	47.60505	2016-03-18 00:00:00	http://www.realtor.com/realestateandhomes-detail/1000-1st-Ave-Unit-2301_Seattle_WA_98104_M18149-83729	{\r\n  "interior_features": ["Cable television available", "Ceramic tile flooring", "Garbage disposal",  "Handicap access", "Hardwood floors",  "Wall to wall carpeting",  "Walk-in closet(s)",  "Elevator(s)", "Exterior Features"],\r\n\r\n  "exterior_features":\r\n  ["Metal exterior",  "Balcony",  "Outdoor hot tub",  "Heating Features"],\r\n\r\n  "heating_features":\r\n  ["Forced air heat,Natural gas heat"],\r\n\r\n  "room_description":\r\n  ["2 total full bath(s)", "1 total half bath"],\r\n\r\n  "unit_features":\r\n  ["Cooling features: Central A/C"],\r\n\r\n  "location":\r\n  ["Area: Downtown", "Subdivision: Madison Tower"],\r\n\r\n  "view":\r\n  ["View", "Waterfront features: Lot on or near bay"],\r\n\r\n  "school":\r\n  ["School District: Seattle"],\r\n\r\n  "fireplace":\r\n  ["Fireplace"]\r\n}
\.


--
-- Name: main_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('main_id_seq', 1, true);


--
-- Data for Name: schools; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY schools (id, main_id, score, name, grades, distance) FROM stdin;
1	1	NR	Special Education Service School	PK-12	0.9 mi
2	1	4	Lowell Elementary School	PK-5	1.6 mi
3	1	8	Mcclure Middle School	6-8	2.4 mi
4	1	6	Garfield High School	9-12	1.6 mi
5	1	NR	Special Education Service School	PK-12	0.9 mi
6	1	4	Lowell Elementary School	PK-5	1.6 mi
7	1	8	Mcclure Middle School	6-8	2.4 mi
8	1	6	Garfield High School	9-12	1.6 mi
\.


--
-- Name: schools_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('schools_id_seq', 8, true);


--
-- Name: schools_main_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('schools_main_id_seq', 1, false);


--
-- Name: images_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY images
    ADD CONSTRAINT images_pkey PRIMARY KEY (id);


--
-- Name: listing_provider_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY listing_provider
    ADD CONSTRAINT listing_provider_pkey PRIMARY KEY (id);


--
-- Name: main_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY main
    ADD CONSTRAINT main_pkey PRIMARY KEY (id);


--
-- Name: schools_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY schools
    ADD CONSTRAINT schools_pkey PRIMARY KEY (id);


--
-- Name: images_main_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY images
    ADD CONSTRAINT images_main_id_fkey FOREIGN KEY (main_id) REFERENCES main(id);


--
-- Name: listing_provider_main_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY listing_provider
    ADD CONSTRAINT listing_provider_main_id_fkey FOREIGN KEY (main_id) REFERENCES main(id);


--
-- Name: schools_main_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY schools
    ADD CONSTRAINT schools_main_id_fkey FOREIGN KEY (main_id) REFERENCES main(id);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

