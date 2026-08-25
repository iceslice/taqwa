--
-- PostgreSQL database dump
--

\restrict XrhNpJdG7DKQzqVdgjYgZjX8Ehm4NiPFnYel19kVMFP3lc81TfEqae096kEHkzj

-- Dumped from database version 18.3
-- Dumped by pg_dump version 18.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: services_service; Type: TABLE DATA; Schema: public; Owner: taqwa_user
--

COPY public.services_service (id, category, title, title_en, title_bn, title_ar, title_ur, title_fa, title_ms, title_fr, title_ru, title_zh_hans, title_es, slug, summary, summary_en, summary_bn, summary_ar, summary_ur, summary_fa, summary_ms, summary_fr, summary_ru, summary_zh_hans, summary_es, description, description_en, description_bn, description_ar, description_ur, description_fa, description_ms, description_fr, description_ru, description_zh_hans, description_es, icon, is_active, "order") FROM stdin;
1	study_abroad	Study Abroad Counseling for Free	Study Abroad Counseling for Free	\N	\N	\N	\N	\N	\N	\N	\N	\N	study-abroad-counseling	Personalized university and course guidance from application to acceptance.	Personalized university and course guidance from application to acceptance.	\N	\N	\N	\N	\N	\N	\N	\N	\N	Personalized university and course guidance from application to acceptance.	Personalized university and course guidance from application to acceptance.											t	0
2	visa	Visa Application Support	Visa Application Support	\N	\N	\N	\N	\N	\N	\N	\N	\N	visa-application-support	Visa Application Support	Visa Application Support	\N	\N	\N	\N	\N	\N	\N	\N	\N	Visa Application Support...	Visa Application Support...											t	0
3	scholarship	Scholarship Guidance	Scholarship Guidance	\N	\N	\N	\N	\N	\N	\N	\N	\N	scholarship-guidance	Scholarship Guidance	Scholarship Guidance	\N	\N	\N	\N	\N	\N	\N	\N	\N	Scholarship Guidance...	Scholarship Guidance...											t	0
\.


--
-- Data for Name: universities_country; Type: TABLE DATA; Schema: public; Owner: taqwa_user
--

COPY public.universities_country (id, name, name_en, name_bn, name_ar, name_ur, name_fa, name_ms, name_fr, name_ru, name_zh_hans, name_es, slug, flag_emoji) FROM stdin;
1	Malaysia	Malaysia	\N	\N	\N	\N	\N	\N	\N	\N	\N	malaysia	
\.


--
-- Name: services_service_id_seq; Type: SEQUENCE SET; Schema: public; Owner: taqwa_user
--

SELECT pg_catalog.setval('public.services_service_id_seq', 3, true);


--
-- Name: universities_country_id_seq; Type: SEQUENCE SET; Schema: public; Owner: taqwa_user
--

SELECT pg_catalog.setval('public.universities_country_id_seq', 1, true);


--
-- PostgreSQL database dump complete
--

\unrestrict XrhNpJdG7DKQzqVdgjYgZjX8Ehm4NiPFnYel19kVMFP3lc81TfEqae096kEHkzj

