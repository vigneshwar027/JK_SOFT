
CREATE DATABASE [VISA_BULLETIN_IMPORT]

USE [VISA_BULLETIN_IMPORT]

CREATE TABLE [dbo].[VisaBulletinData](
	[Visa_Bulletin_Month_and_Year] [nvarchar](max) NULL,
	[Priority_Category] [nvarchar](max) NULL,
	[Priority_Country] [nvarchar](max) NULL,
	[Priority_Type] [nvarchar](max) NULL,
	[Priority_Date] [datetime] NULL,
	[Priority_Processing_Category] [nvarchar](max) NULL,
	[USCIS_Filing_Cut_off] [nvarchar](max) NULL
)