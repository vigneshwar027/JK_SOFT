USE [master]
GO
/****** Object:  Database [immilyticsi140]    Script Date: 5/23/2022 5:47:36 AM ******/
CREATE DATABASE [immilyticsi140]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'immilyticsi140', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\immilyticsi140.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'immilyticsi140_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\immilyticsi140_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO
ALTER DATABASE [immilyticsi140] SET COMPATIBILITY_LEVEL = 150
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [immilyticsi140].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [immilyticsi140] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [immilyticsi140] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [immilyticsi140] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [immilyticsi140] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [immilyticsi140] SET ARITHABORT OFF 
GO
ALTER DATABASE [immilyticsi140] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [immilyticsi140] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [immilyticsi140] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [immilyticsi140] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [immilyticsi140] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [immilyticsi140] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [immilyticsi140] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [immilyticsi140] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [immilyticsi140] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [immilyticsi140] SET  DISABLE_BROKER 
GO
ALTER DATABASE [immilyticsi140] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [immilyticsi140] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [immilyticsi140] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [immilyticsi140] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [immilyticsi140] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [immilyticsi140] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [immilyticsi140] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [immilyticsi140] SET RECOVERY FULL 
GO
ALTER DATABASE [immilyticsi140] SET  MULTI_USER 
GO
ALTER DATABASE [immilyticsi140] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [immilyticsi140] SET DB_CHAINING OFF 
GO
ALTER DATABASE [immilyticsi140] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [immilyticsi140] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [immilyticsi140] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [immilyticsi140] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
EXEC sys.sp_db_vardecimal_storage_format N'immilyticsi140', N'ON'
GO
ALTER DATABASE [immilyticsi140] SET QUERY_STORE = OFF
GO
USE [immilyticsi140]
GO
/****** Object:  Table [dbo].[Beneficiary]    Script Date: 5/23/2022 5:47:36 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Beneficiary](
	[BeneficiaryId] [bigint] IDENTITY(1,1) NOT NULL,
	[BeneficiaryXref] [nvarchar](max) NOT NULL,
	[OrganizationId] [bigint] NULL,
	[PetitionerId] [bigint] NULL,
	[PrimaryBeneficiaryXref] [nvarchar](max) NULL,
	[PrimaryBeneficiaryLastName] [nvarchar](max) NULL,
	[PrimaryBeneficiaryFirstName] [nvarchar](max) NULL,
	[CitizenshipCountry] [nvarchar](max) NULL,
	[RelationType] [nvarchar](max) NULL,
	[IsActive] [bit] NULL,
	[InactiveDate] [datetime] NULL,
	[FirmClientNumber] [nvarchar](max) NULL,
	[BeneficiaryType] [nvarchar](max) NULL,
	[Prefix] [nvarchar](max) NULL,
	[FirstName] [nvarchar](max) NULL,
	[MiddleName] [nvarchar](max) NULL,
	[LastName] [nvarchar](max) NULL,
	[Suffix] [nvarchar](max) NULL,
	[OtherFirstName] [nvarchar](max) NULL,
	[OtherMiddleName] [nvarchar](max) NULL,
	[OtherLastName] [nvarchar](max) NULL,
	[WorkEmail] [nvarchar](max) NULL,
	[PersonalEmail] [nvarchar](max) NULL,
	[HomePhone] [nvarchar](max) NULL,
	[WorkPhone] [nvarchar](max) NULL,
	[Mobile] [nvarchar](max) NULL,
	[IsRovingEmployee] [bit] NULL,
	[IsWorkOffsite] [bit] NULL,
	[IsWorkAtMultipleSites] [bit] NULL,
	[Gender] [nvarchar](max) NULL,
	[SsnNumber] [nvarchar](max) NULL,
	[AlienNumber] [nvarchar](max) NULL,
	[BirthDate] [datetime] NULL,
	[BirthCity] [nvarchar](max) NULL,
	[BirthStateProvince] [nvarchar](max) NULL,
	[BirthCountry] [nvarchar](max) NULL,
	[MaritalStatus] [nvarchar](max) NULL,
	[SpouseBirthCountry] [nvarchar](max) NULL,
	[IsInRemovalProceeding] [bit] NULL,
	[MostRecentUSEntryDate] [datetime] NULL,
	[MostRecentUSEntryCity] [nvarchar](max) NULL,
	[MostRecentUSEntryState] [nvarchar](max) NULL,
	[HasMostRecentUSEntryAdmitted] [bit] NULL,
	[MostRecentUSDepartureDate] [datetime] NULL,
	[I94FirstName] [nvarchar](max) NULL,
	[I94MiddleName] [nvarchar](max) NULL,
	[I94LastName] [nvarchar](max) NULL,
	[I94Number] [nvarchar](max) NULL,
	[I94Status] [nvarchar](max) NULL,
	[I94ValidFromDate] [datetime] NULL,
	[I94ExpirationDate] [datetime] NULL,
	[MostRecentUSI94EntryStatus] [nvarchar](max) NULL,
	[MostRecentI797Status] [nvarchar](max) NULL,
	[MostRecentI797ValidFromDate] [datetime] NULL,
	[MaxOutDateNote] [nvarchar](max) NULL,
	[I797ExpirationDate] [datetime] NULL,
	[I797ReceiptNumber] [nvarchar](max) NULL,
	[MostRecentI797IssueApprovalDate] [datetime] NULL,
	[InitialHlEntryDate] [datetime] NULL,
	[FinalNivDate] [datetime] NULL,
	[FifthYearEndDate] [datetime] NULL,
	[EndorsedI129sExpirationDate] [datetime] NULL,
	[FormI129sRequestedExpirationDate] [datetime] NULL,
	[VisaPedDate] [datetime] NULL,
	[VisaIssueApprovalDate] [datetime] NULL,
	[VisaCategory] [nvarchar](max) NULL,
	[VisaType] [nvarchar](max) NULL,
	[VisaValidFromDate] [datetime] NULL,
	[VisaExpirationDate] [datetime] NULL,
	[PassportFirstName] [nvarchar](max) NULL,
	[PassportMiddleName] [nvarchar](max) NULL,
	[PassportLastName] [nvarchar](max) NULL,
	[PassportNumber] [nvarchar](max) NULL,
	[PassportCountry] [nvarchar](max) NULL,
	[PassportIssuedInCountry] [nvarchar](max) NULL,
	[PassportIssueApprovalDate] [datetime] NULL,
	[PassportValidFromDate] [datetime] NULL,
	[PassportExpirationDate] [datetime] NULL,
	[MostRecentI94EntryPassportNumber] [nvarchar](max) NULL,
	[SevisNumber] [nvarchar](max) NULL,
	[CPTValidFromDate] [datetime] NULL,
	[CPTExpirationDate] [datetime] NULL,
	[F1OptValidFromDate] [datetime] NULL,
	[F1OptExpirationDate] [datetime] NULL,
	[IsStemEligible] [bit] NULL,
	[F1StemOptValidFromDate] [datetime] NULL,
	[F1StemOptExpirationDate] [datetime] NULL,
	[HasPreviouslyHeldF1Status] [bit] NULL,
	[EadType] [nvarchar](max) NULL,
	[EadNumber] [nvarchar](max) NULL,
	[EadValidFromDate] [datetime] NULL,
	[EadExpirationDate] [datetime] NULL,
	[I140FileByDate] [datetime] NULL,
	[AdvanceParoleValidFromDate] [datetime] NULL,
	[AdvanceParoleExpirationDate] [datetime] NULL,
	[EadApValidFromDate] [datetime] NULL,
	[EadApExpirationDate] [datetime] NULL,
	[GreenCardValidFromDate] [datetime] NULL,
	[GreenCardExpirationDate] [datetime] NULL,
	[ReEntryPermitValidFromDate] [datetime] NULL,
	[ReEntryPermitExpirationDate] [datetime] NULL,
	[I90FilingEligibilityDate] [datetime] NULL,
	[I751FilingEligibilityDate] [datetime] NULL,
	[N400FilingEligibilityDate] [datetime] NULL,
	[HasPreviouslyHeldJVisaStatus] [bit] NULL,
	[PreviouslyHeldJVisaType] [nvarchar](max) NULL,
	[JVisaType] [nvarchar](max) NULL,
	[JVisaStatusValidFromDate] [datetime] NULL,
	[JVisaStatusExpirationDate] [datetime] NULL,
	[Ds2019IssueApprovalDate] [datetime] NULL,
	[Ds2019ValidFromDate] [datetime] NULL,
	[Ds2019ExpirationDate] [datetime] NULL,
	[HasHomeStayRequirement] [bit] NULL,
	[HasHomeStayRequirementWaiverReceived] [bit] NULL,
	[PrProcessActualStartDate] [datetime] NULL,
	[PrProcessTargetStartDate] [datetime] NULL,
	[HasPrProcessInitiated] [bit] NULL,
	[PermCaseFiledDate] [datetime] NULL,
	[PermCaseApprovedDate] [datetime] NULL,
	[PermPriorityDate] [datetime] NULL,
	[PermPriorityCategory] [nvarchar](max) NULL,
	[PermPriorityCountry] [nvarchar](max) NULL,
	[PermEta9089ExpirationDate] [datetime] NULL,
	[I140CaseFiledDate] [datetime] NULL,
	[I140CaseApprovedDate] [datetime] NULL,
	[I140PetitionerName] [nvarchar](max) NULL,
	[I140PriorityDate] [datetime] NULL,
	[I140PriorityCategory] [nvarchar](max) NULL,
	[I140PriorityCountry] [nvarchar](max) NULL,
	[HasPriorEmployerApprovedI140] [bit] NULL,
	[PriorEmployerI140PetitionerName] [nvarchar](max) NULL,
	[PriorEmployerI140PriorityDate] [datetime] NULL,
	[PriorEmployerI140PriorityCategory] [nvarchar](max) NULL,
	[PriorEmployerI140PriorityCountry] [nvarchar](max) NULL,
	[AosCaseFiledDate] [datetime] NULL,
	[AosCaseApprovedDate] [datetime] NULL,
	[ManagingAttorney] [nvarchar](max) NULL,
	[TravelDocumentIssueCountry] [nvarchar](max) NULL,
	[MostRecentUSEntryTravelDocumentNumber] [nvarchar](max) NULL,
	[NonimmigrantVisaNumber] [nvarchar](max) NULL,
	[Ethnicity] [nvarchar](max) NULL,
	[Race] [nvarchar](max) NULL,
	[HeightFeet] [int] NULL,
	[HeightInches] [int] NULL,
	[EyeColor] [nvarchar](max) NULL,
	[HairColor] [nvarchar](max) NULL,
	[WeightLbs] [int] NULL,
	[ImmigrationStatusValidFromDate] [datetime] NULL,
	[ImmigrationStatusExpirationDate] [nvarchar](max) NULL,
	[MostRecentPassportLastName] [nvarchar](max) NULL,
	[MostRecentPassportFirstName] [nvarchar](max) NULL,
	[MostRecentPassportNumber] [nvarchar](max) NULL,
	[MostRecentPassportIssuingCountry] [nvarchar](max) NULL,
	[MostRecentPassportMiddleName] [nvarchar](max) NULL,
	[MostRecentPassportValidFromDate] [datetime] NULL,
	[EADAPType] [nvarchar](max) NULL,
	[MostRecentPassportExpirationDate] [datetime] NULL,
	[ImmigrationStatus] [nvarchar](max) NULL,
	[WeightKg] [int] NULL,
	[SourceCreatedBy] [nvarchar](max) NULL,
	[SourceCreatedDate] [datetime] NULL,
	[SourceUpdatedBy] [nvarchar](max) NULL,
	[SourceUpdatedDate] [datetime] NULL,
	[CreatedBy] [nvarchar](max) NULL,
	[CreatedDate] [datetime] NULL,
	[UpdatedBy] [nvarchar](max) NULL,
	[UpdatedDate] [datetime] NULL,
	[from_name] [nvarchar](max) NULL,
	[is_primary_beneficiary] [int] NOT NULL,
 CONSTRAINT [PK__Benefici__3FBA95F566CD4BAD] PRIMARY KEY CLUSTERED 
(
	[BeneficiaryId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[BeneficiaryAddress]    Script Date: 5/23/2022 5:47:36 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[BeneficiaryAddress](
	[BeneficiaryAddressId] [bigint] IDENTITY(1,1) NOT NULL,
	[BeneficiaryId] [bigint] NOT NULL,
	[AddressCountry] [nvarchar](max) NULL,
	[AddressType] [nvarchar](max) NULL,
	[AddressUnitType] [nvarchar](max) NULL,
	[Address1] [nvarchar](255) NULL,
	[AptSteFlr] [char](10) NULL,
	[Address2] [nvarchar](255) NULL,
	[City] [nvarchar](75) NULL,
	[County] [nvarchar](75) NULL,
	[StateProvince] [nvarchar](75) NULL,
	[ZipCode] [nvarchar](15) NULL,
	[Country] [nvarchar](75) NULL,
	[AddressFromDate] [datetime] NULL,
	[AddressToDate] [datetime] NULL,
	[IsLastResidenceAbroad] [bit] NULL,
	[SourceCreatedBy] [nvarchar](50) NULL,
	[SourceCreatedDate] [datetime] NULL,
	[SourceUpdatedBy] [nvarchar](50) NULL,
	[SourceUpdatedDate] [datetime] NULL,
	[CreatedBy] [nvarchar](50) NULL,
	[CreatedDate] [datetime] NULL,
	[UpdatedBy] [nvarchar](50) NULL,
	[UpdatedDate] [datetime] NULL,
 CONSTRAINT [PK__Benefici__A0E4F3B5F0498ACE] PRIMARY KEY CLUSTERED 
(
	[BeneficiaryAddressId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[BeneficiaryEducation]    Script Date: 5/23/2022 5:47:36 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[BeneficiaryEducation](
	[BeneficiaryEducationId] [bigint] IDENTITY(1,1) NOT NULL,
	[BeneficiaryId] [bigint] NOT NULL,
	[CollegeUniversityName] [nvarchar](350) NULL,
	[DegreeType] [nvarchar](150) NULL,
	[FieldOfStudy] [nvarchar](255) NULL,
	[DegreeReceivedDate] [datetime] NULL,
	[IsHighestDegree] [bit] NULL,
	[USOrForeignDegree] [nvarchar](50) NULL,
	[ProgramLength] [int] NULL,
	[Address1] [nvarchar](255) NULL,
	[AptSteFlr] [char](10) NULL,
	[Address2] [nvarchar](255) NULL,
	[Address_City] [nvarchar](75) NULL,
	[StateProvince] [nvarchar](75) NULL,
	[ZipCode] [nvarchar](15) NULL,
	[Country] [nvarchar](75) NULL,
	[SourceCreatedBy] [nvarchar](50) NULL,
	[SourceCreatedDate] [datetime] NULL,
	[SourceUpdatedBy] [nvarchar](50) NULL,
	[SourceUpdatedDate] [datetime] NULL,
	[CreatedBy] [nvarchar](50) NULL,
	[CreatedDate] [datetime] NULL,
	[UpdatedBy] [nvarchar](50) NULL,
	[UpdatedDate] [datetime] NULL,
PRIMARY KEY CLUSTERED 
(
	[BeneficiaryEducationId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[BeneficiaryEmployment]    Script Date: 5/23/2022 5:47:36 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[BeneficiaryEmployment](
	[BeneficiaryEmploymentId] [int] IDENTITY(1,1) NOT NULL,
	[BeneficiaryId] [bigint] NOT NULL,
	[EmployeeId] [nvarchar](max) NULL,
	[EmploymentType] [nvarchar](max) NULL,
	[EmployeeStatus] [nvarchar](max) NULL,
	[EmployerName] [nvarchar](max) NULL,
	[HireDate] [datetime] NULL,
	[TerminationDate] [datetime] NULL,
	[ReHireDate] [datetime] NULL,
	[IsCurrent] [bit] NULL,
	[TerminationReason] [nvarchar](max) NULL,
	[OverallYearsofExperience] [int] NULL,
	[JobTitle] [nvarchar](max) NULL,
	[FunctionalJobTitleInternal] [nvarchar](max) NULL,
	[Address1] [nvarchar](max) NULL,
	[AptSteFlr] [nvarchar](max) NULL,
	[Address2] [nvarchar](max) NULL,
	[City] [nvarchar](max) NULL,
	[StateProvince] [nvarchar](max) NULL,
	[ZipCode] [nvarchar](max) NULL,
	[Country] [nvarchar](max) NULL,
	[JobDuties] [nvarchar](max) NULL,
	[HrbpId] [nvarchar](max) NULL,
	[HrbpFirstName] [nvarchar](max) NULL,
	[HrbpMiddleName] [nvarchar](max) NULL,
	[HrbpLastName] [nvarchar](max) NULL,
	[HrbpEmail] [nvarchar](max) NULL,
	[SupervisorManagerId] [nvarchar](max) NULL,
	[SupervisorManagerFirstName] [nvarchar](max) NULL,
	[SupervisorManagerMiddleName] [nvarchar](max) NULL,
	[SupervisorManagerLastName] [nvarchar](max) NULL,
	[SupervisorManagerEmail] [nvarchar](max) NULL,
	[DepartmentCode] [nvarchar](max) NULL,
	[DepartmentName] [nvarchar](max) NULL,
	[BusinessUnit] [nvarchar](max) NULL,
	[CostCenterCode] [nvarchar](max) NULL,
	[CostCenterCodeName] [nvarchar](max) NULL,
	[ProjectCode] [nvarchar](max) NULL,
	[ProjectName] [nvarchar](max) NULL,
	[EndClient] [nvarchar](max) NULL,
	[SourceCreatedBy] [nvarchar](max) NULL,
	[SourceCreatedDate] [datetime] NULL,
	[SourceUpdatedBy] [nvarchar](max) NULL,
	[SourceUpdatedDate] [datetime] NULL,
	[CreatedBy] [nvarchar](max) NULL,
	[CreatedDate] [datetime] NULL,
	[UpdatedBy] [nvarchar](max) NULL,
	[UpdatedDate] [datetime] NULL,
 CONSTRAINT [PK__Benefici__0C7056D5DAB60B79] PRIMARY KEY CLUSTERED 
(
	[BeneficiaryEmploymentId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[BeneficiaryFamily]    Script Date: 5/23/2022 5:47:36 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[BeneficiaryFamily](
	[BeneficiaryFamilyId] [bigint] IDENTITY(1,1) NOT NULL,
	[BeneficiaryId] [bigint] NOT NULL,
	[RelationBeneficiaryId] [bigint] NOT NULL,
	[RelationType] [nvarchar](100) NOT NULL,
	[SourceCreatedBy] [nvarchar](50) NULL,
	[SourceCreatedDate] [datetime] NULL,
	[SourceUpdatedBy] [nvarchar](50) NULL,
	[SourceUpdatedDate] [datetime] NULL,
	[CreatedBy] [nvarchar](50) NULL,
	[CreatedDate] [datetime] NULL,
	[UpdatedBy] [nvarchar](50) NULL,
	[UpdatedDate] [datetime] NULL,
PRIMARY KEY CLUSTERED 
(
	[BeneficiaryFamilyId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[BeneficiaryPriorityDate]    Script Date: 5/23/2022 5:47:36 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[BeneficiaryPriorityDate](
	[BeneficiaryId] [bigint] NOT NULL,
	[Priority1Date] [datetime] NULL,
	[Priority1Category] [nvarchar](75) NULL,
	[Priority1Country] [nvarchar](75) NULL,
	[Priority2Date] [datetime] NULL,
	[Priority2Category] [nvarchar](75) NULL,
	[Priority2Country] [nvarchar](75) NULL,
	[Priority3Date] [datetime] NULL,
	[Priority3Category] [nvarchar](75) NULL,
	[Priority3Country] [nvarchar](75) NULL,
	[Priority4Date] [datetime] NULL,
	[Priority4Category] [nvarchar](75) NULL,
	[Priority4Country] [nvarchar](75) NULL,
	[Priority5Date] [datetime] NULL,
	[Priority5Category] [nvarchar](75) NULL,
	[Priority5Country] [nvarchar](75) NULL,
	[SourceCreatedBy] [nvarchar](50) NULL,
	[SourceCreatedDate] [datetime] NULL,
	[SourceUpdatedBy] [nvarchar](50) NULL,
	[SourceUpdatedDate] [datetime] NULL,
	[CreatedBy] [nvarchar](50) NULL,
	[CreatedDate] [datetime] NULL,
	[UpdatedBy] [nvarchar](50) NULL,
	[UpdatedDate] [datetime] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Case]    Script Date: 5/23/2022 5:47:36 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Case](
	[CaseId] [bigint] IDENTITY(1,1) NOT NULL,
	[CaseXref] [nvarchar](max) NOT NULL,
	[OrganizationId] [bigint] NULL,
	[BeneficiaryId] [bigint] NOT NULL,
	[CaseType] [nvarchar](max) NULL,
	[RFEAuditDueDate] [datetime] NULL,
	[RFEAuditSubmittedDate] [datetime] NULL,
	[RFEAuditReceivedDate] [datetime] NULL,
	[CasePetitionName] [nvarchar](max) NULL,
	[PetitionerSponsorId] [bigint] NULL,
	[ServiceType] [nvarchar](max) NULL,
	[OriginatingCountry] [nvarchar](max) NULL,
	[DestinationCountry] [nvarchar](max) NULL,
	[CaseDescription] [nvarchar](max) NULL,
	[CaseOpenDate] [datetime] NULL,
	[IsPPEligibleAtFiling] [bit] NULL,
	[HasFiledByPP] [bit] NULL,
	[PPType] [nvarchar](max) NULL,
	[CaseFiledDate] [datetime] NULL,
	[ReceiptDateReceivedByGovt] [datetime] NULL,
	[ReceiptNumber] [nvarchar](max) NULL,
	[ReceiptStatus] [nvarchar](max) NULL,
	[CaseApprovedDate] [datetime] NULL,
	[CaseValidFromDate] [datetime] NULL,
	[CaseExpirationDate] [datetime] NULL,
	[PriorityDate] [datetime] NULL,
	[PriorityCategory] [nvarchar](max) NULL,
	[PriorityCountry] [nvarchar](max) NULL,
	[PetitionXref] [nvarchar](max) NULL,
	[CasePrimaryCaseManager] [nvarchar](max) NULL,
	[CasePrimaryAttorney] [nvarchar](max) NULL,
	[CaseReviewingAttorney] [nvarchar](max) NULL,
	[CaseWithdrawnDate] [datetime] NULL,
	[CaseClosedDate] [datetime] NULL,
	[CaseDeniedDate] [datetime] NULL,
	[DenialReason] [nvarchar](max) NULL,
	[CaseComments] [nvarchar](max) NULL,
	[PrimaryCaseStatus] [nvarchar](max) NULL,
	[SecondaryCaseStatus] [nvarchar](max) NULL,
	[SecondaryCaseStatusDate] [datetime] NULL,
	[LastStepCompleted] [text] NULL,
	[LastStepCompletedDate] [datetime] NULL,
	[NextStepAction] [nvarchar](max) NULL,
	[NextStepActionDueDate] [datetime] NULL,
	[NextStepActionToBeTakenBy] [nvarchar](max) NULL,
	[NotesInternal] [nvarchar](max) NULL,
	[NotesExternal] [nvarchar](max) NULL,
	[NotesConfidential] [nvarchar](max) NULL,
	[AttorneyPrimaryIdXref] [nvarchar](max) NULL,
	[AttorneyPrimaryEMPId] [nvarchar](max) NULL,
	[AttorneyPrimaryFirstName] [nvarchar](max) NULL,
	[AttorneyPrimaryMiddleName] [nvarchar](max) NULL,
	[AttorneyPrimaryLastName] [nvarchar](max) NULL,
	[AttorneyPrimaryCaseCreditPercentage] [int] NULL,
	[Attorney2IdXref] [nvarchar](max) NULL,
	[Attorney2EMPId] [nvarchar](max) NULL,
	[Attorney2FirstName] [nvarchar](max) NULL,
	[Attorney2MiddleName] [nvarchar](max) NULL,
	[Attorney2LastName] [nvarchar](max) NULL,
	[CaseWorkerPrimaryCaseCreditPercentage] [int] NULL,
	[CaseWorkerPrimaryIdXref] [nvarchar](max) NULL,
	[CaseWorkerPrimaryEMPId] [nvarchar](max) NULL,
	[CaseWorkerPrimaryFirstName] [nvarchar](max) NULL,
	[CaseWorkerPrimaryMiddleName] [nvarchar](max) NULL,
	[CaseWorkerPrimaryLastName] [nvarchar](max) NULL,
	[CaseWorker2CaseCreditPercentage] [int] NULL,
	[CaseWorker2IdXref] [nvarchar](max) NULL,
	[CaseWorker2EMPId] [nvarchar](max) NULL,
	[CaseWorker2FirstName] [nvarchar](max) NULL,
	[CaseWorker2MiddleName] [nvarchar](max) NULL,
	[CaseWorker2LastName] [nvarchar](max) NULL,
	[CaseWorker3CaseCreditPercentage] [int] NULL,
	[CaseWorker3IdXref] [nvarchar](max) NULL,
	[CaseWorker3EMPId] [nvarchar](max) NULL,
	[CaseWorker3FirstName] [nvarchar](max) NULL,
	[CaseWorker3MiddleName] [nvarchar](max) NULL,
	[CaseWorker3LastName] [nvarchar](max) NULL,
	[CaseInitiationDate] [datetime] NULL,
	[AllDocsReceivedDate] [datetime] NULL,
	[HrbpId] [nvarchar](max) NULL,
	[HrbpFirstName] [nvarchar](max) NULL,
	[HrbpMiddleName] [nvarchar](max) NULL,
	[HrbpLastName] [nvarchar](max) NULL,
	[HrbpEmail] [nvarchar](max) NULL,
	[SupervisorManagerId] [nvarchar](max) NULL,
	[SupervisorManagerFirstName] [nvarchar](max) NULL,
	[SupervisorManagerMiddleName] [nvarchar](max) NULL,
	[SupervisorManagerLastName] [nvarchar](max) NULL,
	[SupervisorManagerEmail] [nvarchar](max) NULL,
	[DepartmentCode] [nvarchar](max) NULL,
	[DepartmentName] [nvarchar](max) NULL,
	[BusinessUnit] [nvarchar](max) NULL,
	[CostCenterCode] [nvarchar](max) NULL,
	[CostCenterCodeName] [nvarchar](max) NULL,
	[ProjectCode] [nvarchar](max) NULL,
	[ProjectName] [nvarchar](max) NULL,
	[SourceCreatedBy] [nvarchar](max) NULL,
	[SourceCreatedDate] [datetime] NULL,
	[SourceUpdatedBy] [nvarchar](max) NULL,
	[SourceUpdatedDate] [datetime] NULL,
	[CreatedBy] [nvarchar](max) NULL,
	[CreatedDate] [datetime] NULL,
	[UpdatedBy] [nvarchar](max) NULL,
	[UpdatedDate] [datetime] NULL,
	[from_name] [nvarchar](max) NULL,
 CONSTRAINT [PK__Case__6CAE524CABDB0583] PRIMARY KEY CLUSTERED 
(
	[CaseId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[CaseETA9089]    Script Date: 5/23/2022 5:47:36 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[CaseETA9089](
	[PERMDOLCaseNumber] [nvarchar](255) NULL,
	[PERMFilingDate] [date] NULL,
	[PERMCertificationDate] [date] NULL,
	[PERMValidFrom] [date] NULL,
	[PERMValidTo] [date] NULL,
	[PetitionerName] [nvarchar](255) NULL,
	[PetitionerAddress1] [nvarchar](255) NULL,
	[PetitionerAddress2] [nvarchar](255) NULL,
	[PetitionerCity] [nvarchar](255) NULL,
	[PetitionerState] [nvarchar](255) NULL,
	[PetitionerZipCode] [nvarchar](255) NULL,
	[PetitionerCountry] [nvarchar](255) NULL,
	[PetitionerPhone] [nvarchar](255) NULL,
	[PetitionerPhoneExt] [nvarchar](255) NULL,
	[NumberOfEmployees] [int] NULL,
	[YearCommencedBusiness] [int] NULL,
	[FEIN] [nvarchar](255) NULL,
	[NAICSCode] [int] NULL,
	[PetitionerContactLastName] [nvarchar](255) NULL,
	[PetitionerContactFirstName] [nvarchar](255) NULL,
	[PetitionerContactMiddleInitial] [nvarchar](255) NULL,
	[PetitionerContactAddress1] [nvarchar](255) NULL,
	[PetitonerContactAddress2] [nvarchar](255) NULL,
	[PetitionerContactCity] [nvarchar](255) NULL,
	[PetitionerContactState] [nvarchar](255) NULL,
	[PetitionerContactZipCode] [nvarchar](255) NULL,
	[PetitionerContactCountry] [nvarchar](255) NULL,
	[PetitionerContactPhoneNumber] [nvarchar](255) NULL,
	[PetitionerContactPhoneExt] [nvarchar](255) NULL,
	[PetitionerContactEmail] [nvarchar](255) NULL,
	[AttorneyAgentLastName] [nvarchar](255) NULL,
	[AttorneyAgentFirstName] [nvarchar](255) NULL,
	[AttorneyAgentMiddleInitial] [nvarchar](255) NULL,
	[AttorneyAgentFirmName] [nvarchar](255) NULL,
	[AttorneyAgentFirmFEIN] [nvarchar](255) NULL,
	[AttorneyAgentAddress1] [nvarchar](255) NULL,
	[AttorneyAgentAddress2] [nvarchar](255) NULL,
	[AttorneyAgentCity] [nvarchar](255) NULL,
	[AttorneyAgentState] [nvarchar](255) NULL,
	[AttorneyAgentZipCode] [nvarchar](255) NULL,
	[AttorneyAgentCountry] [nvarchar](255) NULL,
	[AttorneyAgentPhoneNumber] [nvarchar](255) NULL,
	[AttorneyAgentPhoneExt] [nvarchar](255) NULL,
	[AttorneyAgentEmail] [nvarchar](255) NULL,
	[SOCCODE] [nvarchar](255) NULL,
	[JobTitle] [nvarchar](255) NULL,
	[JobDuties] [nvarchar](255) NULL,
	[WorkLocationAddress1] [nvarchar](255) NULL,
	[WorkLocationAddress2] [nvarchar](255) NULL,
	[WorkLocationCity] [nvarchar](255) NULL,
	[WorkLocationState] [nvarchar](255) NULL,
	[WorkLocationZipCode] [nvarchar](255) NULL,
	[OfferedWageFrom] [nvarchar](255) NULL,
	[OfferedWageTo] [nvarchar](255) NULL,
	[OfferedWageType] [nvarchar](255) NULL,
	[BeneficiaryLastName] [nvarchar](255) NULL,
	[BeneficiaryFirstName] [nvarchar](255) NULL,
	[BeneficiaryMiddleName] [nvarchar](255) NULL,
	[BeneficiaryAddress1] [nvarchar](255) NULL,
	[BeneficiaryAddress2] [nvarchar](255) NULL,
	[BeneficiaryAddressCity] [nvarchar](255) NULL,
	[BeneficiaryAddressState] [nvarchar](255) NULL,
	[BeneficiaryAddressZipCode] [nvarchar](255) NULL,
	[BeneficiaryAddressCountry] [nvarchar](255) NULL,
	[BeneficiaryDateofBirth] [date] NULL,
	[BeneficiaryCountryofBirth] [nvarchar](255) NULL,
	[BeneficiaryCountryofCitizenship] [nvarchar](255) NULL,
	[BeneficiaryAlienNumber] [nvarchar](255) NULL,
	[BeneficiaryClassofAdmission] [nvarchar](255) NULL,
	[BeneficiaryI94Number] [nvarchar](255) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[CaseLCA]    Script Date: 5/23/2022 5:47:36 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[CaseLCA](
	[LCACaseNumber] [nvarchar](max) NOT NULL,
	[BeneficiaryXref] [nvarchar](max) NULL,
	[CaseXref] [nvarchar](max) NULL,
	[LCACertificationDate] [datetime] NULL,
	[LCACertificationValidFrom] [datetime] NULL,
	[LCACertificationValidTo] [datetime] NULL,
	[LCACaseStatus] [nvarchar](max) NULL,
	[LCAVisaClassification] [nvarchar](max) NULL,
	[LCAJobTitle] [nvarchar](max) NULL,
	[LCASOCCode] [nvarchar](max) NULL,
	[LCASOCOccupationTitle] [nvarchar](max) NULL,
	[LCAIsFull_TimePosition] [nvarchar](max) NULL,
	[LCAIntendedEmploymentStartDate] [datetime] NULL,
	[LCAIntendedEmploymentEndDate] [datetime] NULL,
	[LCANumberofWorkerPositions] [nvarchar](max) NULL,
	[LCANewEmployment_Count] [nvarchar](max) NULL,
	[LCAContinuationofpreviouslyapprovedemployment] [nvarchar](max) NULL,
	[LCAChangeinpreviouslyapprovedemployment] [nvarchar](max) NULL,
	[LCANewconcurrentemployment] [nvarchar](max) NULL,
	[LCAChangeinemployer] [nvarchar](max) NULL,
	[LCAAmendedpetition] [nvarchar](max) NULL,
	[LCAPetitionerName] [nvarchar](max) NULL,
	[LCAPetitionerFEIN] [nvarchar](max) NULL,
	[LCANAICS] [nvarchar](max) NULL,
	[LCAPointofContact_LastName] [nvarchar](max) NULL,
	[LCAPointofContact_FirstName] [nvarchar](max) NULL,
	[LCAPointofContact_MiddleName] [nvarchar](max) NULL,
	[LCAEmployerRepresentedByAttorney_Agent] [nvarchar](max) NULL,
	[LCAAttorneyorAgent_LastName] [nvarchar](max) NULL,
	[LCAAttorneyorAgent_FirstName] [nvarchar](max) NULL,
	[LCAAttorneyorAgent_MiddleName] [nvarchar](max) NULL,
	[LCAFirm_BusinessName] [nvarchar](max) NULL,
	[LCAFirm_BusinessFEIN] [nvarchar](max) NULL,
	[LCAH_1BDependent] [nvarchar](max) NULL,
	[LCAEmployerWillfulViolator] [nvarchar](max) NULL,
	[LCAONLYH_1B] [nvarchar](max) NULL,
	[LCAStatutoryBasisForExemption] [nvarchar](max) NULL,
	[LCAAppendixAAttached] [nvarchar](max) NULL,
	[LCAPublicDisclosureInfo] [nvarchar](max) NULL,
	[LCAPreparerLastName] [nvarchar](max) NULL,
	[LCAPreparerFirstName] [nvarchar](max) NULL,
	[LCAPreparerMiddleInitial] [nvarchar](max) NULL,
	[LCAPreparerFirm_BusinessName] [nvarchar](max) NULL,
	[LCAPOEI1WorkerNumber] [nvarchar](max) NULL,
	[LCAPOEI1IsSecondaryEntity] [nvarchar](max) NULL,
	[LCAPOEI1LegalBusinessNameofBusinessEntity] [nvarchar](max) NULL,
	[LCAWorkLocation1_Address1] [nvarchar](max) NULL,
	[LCAWorkLocation1_Address2] [nvarchar](max) NULL,
	[LCAWorkLocation1_City] [nvarchar](max) NULL,
	[LCAWorkLocation1_County] [nvarchar](max) NULL,
	[LCAWorkLocation1_State] [nvarchar](max) NULL,
	[LCAWorkLocation1_ZipCode] [nvarchar](max) NULL,
	[LCAWorkLocation1_WageRatePaid_From] [nvarchar](max) NULL,
	[LCAWorkLocation1_WageRatePaid_To] [nvarchar](max) NULL,
	[LCAWorkLocation1_WageRateType] [nvarchar](max) NULL,
	[LCAWorkLocation1_PrevailingWageRate] [nvarchar](max) NULL,
	[LCAWorkLocation1_PrevailingWageRateType] [nvarchar](max) NULL,
	[LCAWorkLocation1_PrevailingWageSource_DOL] [nvarchar](max) NULL,
	[LCAWorkLocation1_PWDTrackingNumber] [nvarchar](max) NULL,
	[LCAWorkLocation1_PrevailingWageSource_OES] [nvarchar](max) NULL,
	[LCAWorkLocation1_OESProgramWageLevel] [nvarchar](max) NULL,
	[LCAWorkLocation1_OESProgramWageSourceYear] [nvarchar](max) NULL,
	[LCAWorkLocation1_PrevailingWageSource_Other] [nvarchar](max) NULL,
	[LCAWorkLocation1_PrevailingWageSource_OtherThanOES_SourceType] [nvarchar](max) NULL,
	[LCAWorkLocation1_PrevailingWageSource_OtherThanOES_SourceYear] [nvarchar](max) NULL,
	[LCAWorkLocation1_PrevailingWageSource_Other_PWSurveyProducer_Publisher] [nvarchar](max) NULL,
	[LCAWorkLocation1_PrevailingWageSource_Other_PWSurveyTitle_Name] [nvarchar](max) NULL,
	[LCAPOEI2WorkerNumber] [nvarchar](max) NULL,
	[LCAPOEI2IsSecondaryEntity] [nvarchar](max) NULL,
	[LCAPOEI2LegalBusinessNameofBusinessEntity] [nvarchar](max) NULL,
	[LCAWorkLocation2_Address1] [nvarchar](max) NULL,
	[LCAWorkLocation2_Address2] [nvarchar](max) NULL,
	[LCAWorkLocation2_City] [nvarchar](max) NULL,
	[LCAWorkLocation2_County] [nvarchar](max) NULL,
	[LCAWorkLocation2_State] [nvarchar](max) NULL,
	[LCAWorkLocation2_ZipCode] [nvarchar](max) NULL,
	[LCAWorkLocation2_WageRatePaid_From] [nvarchar](max) NULL,
	[LCAWorkLocation2_WageRatePaid_To] [nvarchar](max) NULL,
	[LCAWorkLocation2_WageRateType] [nvarchar](max) NULL,
	[LCAWorkLocation2_PrevailingWageRate] [nvarchar](max) NULL,
	[LCAWorkLocation2_PrevailingWageRateType] [nvarchar](max) NULL,
	[LCAWorkLocation2_PrevailingWageSource_DOL] [nvarchar](max) NULL,
	[LCAWorkLocation2_PWDTrackingNumber] [nvarchar](max) NULL,
	[LCAWorkLocation2_PrevailingWageSource_OES] [nvarchar](max) NULL,
	[LCAWorkLocation2_OESProgramWageLevel] [nvarchar](max) NULL,
	[LCAWorkLocation2_OESProgramWageSourceYear] [nvarchar](max) NULL,
	[LCAWorkLocation2_PrevailingWageSource_Other] [nvarchar](max) NULL,
	[LCAWorkLocation2_PrevailingWageSource_OtherThanOES_SourceType] [nvarchar](max) NULL,
	[LCAWorkLocation2_PrevailingWageSource_OtherThanOES_SourceYear] [nvarchar](max) NULL,
	[LCAWorkLocation2_PrevailingWageSource_Other_PWSurveyProducer_Publisher] [nvarchar](max) NULL,
	[LCAWorkLocation2_PrevailingWageSource_Other_PWSurveyTitle_Name] [nvarchar](max) NULL,
	[LCAPOEI3WorkerNumber] [nvarchar](max) NULL,
	[LCAPOEI3IsSecondaryEntity] [nvarchar](max) NULL,
	[LCAPOEI3LegalBusinessNameofBusinessEntity] [nvarchar](max) NULL,
	[LCAWorkLocation3_Address1] [nvarchar](max) NULL,
	[LCAWorkLocation3_Address2] [nvarchar](max) NULL,
	[LCAWorkLocation3_City] [nvarchar](max) NULL,
	[LCAWorkLocation3_County] [nvarchar](max) NULL,
	[LCAWorkLocation3_State] [nvarchar](max) NULL,
	[LCAWorkLocation3_ZipCode] [nvarchar](max) NULL,
	[LCAWorkLocation3_WageRatePaid_From] [nvarchar](max) NULL,
	[LCAWorkLocation3_WageRatePaid_To] [nvarchar](max) NULL,
	[LCAWorkLocation3_WageRateType] [nvarchar](max) NULL,
	[LCAWorkLocation3_PrevailingWageRate] [nvarchar](max) NULL,
	[LCAWorkLocation3_PrevailingWageRateType] [nvarchar](max) NULL,
	[LCAWorkLocation3_PrevailingWageSource_DOL] [nvarchar](max) NULL,
	[LCAWorkLocation3_PWDTrackingNumber] [nvarchar](max) NULL,
	[LCAWorkLocation3_PrevailingWageSource_OES] [nvarchar](max) NULL,
	[LCAWorkLocation3_OESProgramWageLevel] [nvarchar](max) NULL,
	[LCAWorkLocation3_OESProgramWageSourceYear] [nvarchar](max) NULL,
	[LCAWorkLocation3_PrevailingWageSource_Other] [nvarchar](max) NULL,
	[LCAWorkLocation3_PrevailingWageSource_OtherThanOES_SourceType] [nvarchar](max) NULL,
	[LCAWorkLocation3_PrevailingWageSource_OtherThanOES_SourceYear] [nvarchar](max) NULL,
	[LCAWorkLocation3_PrevailingWageSource_Other_PWSurveyProducer_Publisher] [nvarchar](max) NULL,
	[LCAWorkLocation3_PrevailingWageSource_Other_PWSurveyTitle_Name] [nvarchar](max) NULL,
	[LCAPOEI4WorkerNumber] [nvarchar](max) NULL,
	[LCAPOEI4IsSecondaryEntity] [nvarchar](max) NULL,
	[LCAPOEI4LegalBusinessNameofBusinessEntity] [nvarchar](max) NULL,
	[LCAWorkLocation4_Address1] [nvarchar](max) NULL,
	[LCAWorkLocation4_Address2] [nvarchar](max) NULL,
	[LCAWorkLocation4_City] [nvarchar](max) NULL,
	[LCAWorkLocation4_County] [nvarchar](max) NULL,
	[LCAWorkLocation4_State] [nvarchar](max) NULL,
	[LCAWorkLocation4_ZipCode] [nvarchar](max) NULL,
	[LCAWorkLocation4_WageRatePaid_From] [nvarchar](max) NULL,
	[LCAWorkLocation4_WageRatePaid_To] [nvarchar](max) NULL,
	[LCAWorkLocation4_WageRateType] [nvarchar](max) NULL,
	[LCAWorkLocation4_PrevailingWageRate] [nvarchar](max) NULL,
	[LCAWorkLocation4_PrevailingWageRateType] [nvarchar](max) NULL,
	[LCAWorkLocation4_PrevailingWageSource_DOL] [nvarchar](max) NULL,
	[LCAWorkLocation4_PWDTrackingNumber] [nvarchar](max) NULL,
	[LCAWorkLocation4_PrevailingWageSource_OES] [nvarchar](max) NULL,
	[LCAWorkLocation4_OESProgramWageLevel] [nvarchar](max) NULL,
	[LCAWorkLocation4_OESProgramWageSourceYear] [nvarchar](max) NULL,
	[LCAWorkLocation4_PrevailingWageSource_Other] [nvarchar](max) NULL,
	[LCAWorkLocation4_PrevailingWageSource_OtherThanOES_SourceType] [nvarchar](max) NULL,
	[LCAWorkLocation4_PrevailingWageSource_OtherThanOES_SourceYear] [nvarchar](max) NULL,
	[LCAWorkLocation4_PrevailingWageSource_Other_PWSurveyProducer_Publisher] [nvarchar](max) NULL,
	[LCAWorkLocation4_PrevailingWageSource_Other_PWSurveyTitle_Name] [nvarchar](max) NULL,
	[LCAPOEI5WorkerNumber] [nvarchar](max) NULL,
	[LCAPOEI5IsSecondaryEntity] [nvarchar](max) NULL,
	[LCAPOEI5LegalBusinessNameofBusinessEntity] [nvarchar](max) NULL,
	[LCAWorkLocation5_Address1] [nvarchar](max) NULL,
	[LCAWorkLocation5_Address2] [nvarchar](max) NULL,
	[LCAWorkLocation5_City] [nvarchar](max) NULL,
	[LCAWorkLocation5_County] [nvarchar](max) NULL,
	[LCAWorkLocation5_State] [nvarchar](max) NULL,
	[LCAWorkLocation5_ZipCode] [nvarchar](max) NULL,
	[LCAWorkLocation5_WageRatePaid_From] [nvarchar](max) NULL,
	[LCAWorkLocation5_WageRatePaid_To] [nvarchar](max) NULL,
	[LCAWorkLocation5_WageRateType] [nvarchar](max) NULL,
	[LCAWorkLocation5_PrevailingWageRate] [nvarchar](max) NULL,
	[LCAWorkLocation5_PrevailingWageRateType] [nvarchar](max) NULL,
	[LCAWorkLocation5_PrevailingWageSource_DOL] [nvarchar](max) NULL,
	[LCAWorkLocation5_PWDTrackingNumber] [nvarchar](max) NULL,
	[LCAWorkLocation5_PrevailingWageSource_OES] [nvarchar](max) NULL,
	[LCAWorkLocation5_OESProgramWageLevel] [nvarchar](max) NULL,
	[LCAWorkLocation5_OESProgramWageSourceYear] [nvarchar](max) NULL,
	[LCAWorkLocation5_PrevailingWageSource_Other] [nvarchar](max) NULL,
	[LCAWorkLocation5_PrevailingWageSource_OtherThanOES_SourceType] [nvarchar](max) NULL,
	[LCAWorkLocation5_PrevailingWageSource_OtherThanOES_SourceYear] [nvarchar](max) NULL,
	[LCAWorkLocation5_PrevailingWageSource_Other_PWSurveyProducer_Publisher] [nvarchar](max) NULL,
	[LCAWorkLocation5_PrevailingWageSource_Other_PWSurveyTitle_Name] [nvarchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[CaseMilestone]    Script Date: 5/23/2022 5:47:36 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[CaseMilestone](
	[CaseId] [bigint] NOT NULL,
	[CaseInitiatedByPetrDate] [datetime] NULL,
	[CaseCreatedByFirmDate] [datetime] NULL,
	[WelcomeEmailSentDate] [datetime] NULL,
	[DocsChecklistSentToPetrDate] [datetime] NULL,
	[DocsChecklistSentToBnfDate] [datetime] NULL,
	[DocsReceivedFromPetrDate] [datetime] NULL,
	[DocsReceivedFromBnfDate] [datetime] NULL,
	[MinimalInfoDocsReceivedDate] [datetime] NULL,
	[AllInfoDocsReceivedDate] [datetime] NULL,
	[CaseDocsDraftedDate] [datetime] NULL,
	[InitialAttorneyReviewCompletedDate] [datetime] NULL,
	[FinalCaseDocsSentForReviewDate] [datetime] NULL,
	[SignedDocsReceivedDate] [datetime] NULL,
	[FinalAttorneyReviewCompletedDate] [datetime] NULL,
	[CasePacketSentToBnfDate] [datetime] NULL,
	[ReceiptNoticeReceivedDate] [datetime] NULL,
	[ApprovalNoticeReceivedDate] [datetime] NULL,
	[PermMinReqFinalizedDate] [datetime] NULL,
	[PermWorkExpChartSentDate] [datetime] NULL,
	[PermWorkExpChartReceivedDate] [datetime] NULL,
	[PermDraftEvlSentToBnfDate] [datetime] NULL,
	[PermEvlReceivedDate] [datetime] NULL,
	[PermPwrSubmittedDate] [datetime] NULL,
	[PermPwdIssuedDate] [datetime] NULL,
	[ApprovalReceivedFromPetrDate] [datetime] NULL,
	[Eta9089FiledDate] [datetime] NULL,
	[DolCaseNumberReceivedDate] [datetime] NULL,
	[Certified9089ReceivedDate] [datetime] NULL,
	[CreatedBy] [nvarchar](50) NULL,
	[CreatedDate] [datetime] NULL,
	[UpdatedBy] [nvarchar](50) NULL,
	[UpdatedDate] [datetime] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[CasePerm]    Script Date: 5/23/2022 5:47:36 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[CasePerm](
	[CasePermId] [bigint] IDENTITY(1,1) NOT NULL,
	[CaseId] [bigint] NOT NULL,
	[AdAgencyId] [int] NULL,
	[IsAdAgencyActive] [bit] NULL,
	[AdAgencyName] [nvarchar](255) NULL,
	[AdOrderNumber] [nvarchar](255) NULL,
	[PwrDolFiledDate] [datetime] NULL,
	[FileEta9089ReceivedApprovalDate] [datetime] NULL,
	[FirstRecruitmentStartDate] [datetime] NULL,
	[FirstEligibleFilingDate] [datetime] NULL,
	[FilingDeadline] [datetime] NULL,
	[AnticipatedFilingDate] [datetime] NULL,
	[QuietPeriodEndDate] [datetime] NULL,
	[DeadlineRequestRecruitmentReportDate] [datetime] NULL,
	[SwaJobOrderStartDate] [datetime] NULL,
	[SwaJobOrderEndDate] [datetime] NULL,
	[NoticeOfFilingPostingStartDate] [datetime] NULL,
	[NoticeOfFilingPostingEndDate] [datetime] NULL,
	[FirstSundayAdPostingDate] [datetime] NULL,
	[FirstSundayAdPublicationName] [nvarchar](255) NULL,
	[SecondSundayAdPostingDate] [datetime] NULL,
	[SecondSundayAdPublicationName] [nvarchar](255) NULL,
	[JobFairStartDate] [datetime] NULL,
	[JobFairEndDate] [datetime] NULL,
	[JobFairMediaType] [nvarchar](255) NULL,
	[EmployerWebsiteStartDate] [datetime] NULL,
	[EmployerWebsiteEndDate] [datetime] NULL,
	[JobSearchSiteStartDate] [datetime] NULL,
	[JobSearchSiteEndDate] [datetime] NULL,
	[JobSearchSiteMediaType] [nvarchar](255) NULL,
	[EmployeeReferralProgramStartDate] [datetime] NULL,
	[EmployeeReferralProgramEndDate] [datetime] NULL,
	[LocalEthnicNewspaperStartDate] [datetime] NULL,
	[LocalEthnicNewspaperEndDate] [datetime] NULL,
	[LocalEthnicNewspaperMediaType] [nvarchar](255) NULL,
	[OnCampusRecruitingStartDate] [datetime] NULL,
	[OnCampusRecruitingEndDate] [datetime] NULL,
	[OnCampusRecruitingMediaType] [nvarchar](255) NULL,
	[TradeProfessionalOrganizationStartDate] [datetime] NULL,
	[TradeProfessionalOrganizationEndDate] [datetime] NULL,
	[TradeProfessionalOrganizationMediaType] [nvarchar](255) NULL,
	[EmploymentFirmStartDate] [datetime] NULL,
	[EmploymentFirmEndDate] [datetime] NULL,
	[EmploymentFirmMediaType] [nvarchar](255) NULL,
	[CampusPlacementOfficeStartDate] [datetime] NULL,
	[CampusPlacementOfficeEndDate] [datetime] NULL,
	[CampusPlacementOfficeMediaType] [nvarchar](255) NULL,
	[RadioTVStartDate] [datetime] NULL,
	[RadioTVEndDate] [datetime] NULL,
	[RadioTVMediaType] [nvarchar](255) NULL,
	[CreatedBy] [nvarchar](50) NULL,
	[CreatedDate] [datetime] NULL,
	[UpdatedBy] [nvarchar](50) NULL,
	[UpdatedDate] [datetime] NULL,
PRIMARY KEY CLUSTERED 
(
	[CasePermId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[CasePwr]    Script Date: 5/23/2022 5:47:36 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[CasePwr](
	[CasePwrId] [bigint] IDENTITY(1,1) NOT NULL,
	[CaseId] [bigint] NOT NULL,
	[PwrSubmissionDate] [datetime] NULL,
	[PwrTrackingNumber] [nvarchar](20) NULL,
	[PwrSuggestedSocCode] [nvarchar](15) NULL,
	[PwrSuggestedSocOccupationTitle] [nvarchar](255) NULL,
	[PwrWageSource] [nvarchar](75) NULL,
	[PwrWageSourceOtherSurveyName] [nvarchar](255) NULL,
	[PwrWageSourceOtherSurveyPublicationYear] [int] NULL,
	[PwrDeterminationDate] [datetime] NULL,
	[PwrExpirationDate] [datetime] NULL,
	[PwrDolSocCode] [nvarchar](15) NULL,
	[PwrDolWageLevel] [char](5) NULL,
	[PwrDolWage] [int] NULL,
	[PwrDolWagePer] [char](5) NULL,
	[CreatedBy] [nvarchar](50) NULL,
	[CreatedDate] [datetime] NULL,
	[UpdatedBy] [nvarchar](50) NULL,
	[UpdatedDate] [datetime] NULL,
PRIMARY KEY CLUSTERED 
(
	[CasePwrId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[CaseStep]    Script Date: 5/23/2022 5:47:36 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[CaseStep](
	[CaseStepId] [bigint] IDENTITY(1,1) NOT NULL,
	[CaseStepXref] [nvarchar](50) NOT NULL,
	[CaseId] [bigint] NOT NULL,
	[IsStepMilestone] [bit] NULL,
	[CaseStepName] [nvarchar](255) NULL,
	[SourceCreatedBy] [nvarchar](50) NULL,
	[SourceCreatedDate] [datetime] NULL,
	[SourceUpdatedBy] [nvarchar](50) NULL,
	[SourceUpdatedDate] [datetime] NULL,
	[CreatedBy] [nvarchar](50) NULL,
	[CreatedDate] [datetime] NULL,
	[UpdatedBy] [nvarchar](50) NULL,
	[UpdatedDate] [datetime] NULL,
PRIMARY KEY CLUSTERED 
(
	[CaseStepId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ClientDetails]    Script Date: 5/23/2022 5:47:36 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ClientDetails](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[client_name] [varchar](255) NOT NULL,
	[clientShortName] [varchar](255) NULL,
	[organizationName] [nvarchar](255) NULL,
	[organizationXref] [varchar](255) NULL,
	[petitionerName] [nvarchar](255) NULL,
	[petitionerXref] [nvarchar](255) NULL,
	[report_name] [varchar](255) NULL,
	[cadence] [varchar](255) NULL,
	[delivery_day] [varchar](255) NULL,
	[delivery_time] [varchar](255) NULL,
	[recipient_to] [text] NULL,
	[recipient_cc] [text] NULL,
	[no_of_tabs] [int] NULL,
	[special_criteria] [nchar](10) NULL,
	[expiration_report_sent] [int] NULL,
	[expiration_report_sent_on] [varchar](30) NULL,
	[status_report_sent_on] [datetime] NULL,
 CONSTRAINT [PK_ClientDetails] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Contact]    Script Date: 5/23/2022 5:47:36 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Contact](
	[ContactId] [bigint] IDENTITY(1,1) NOT NULL,
	[ContactXref] [nvarchar](50) NOT NULL,
	[ContactLevelId] [bigint] NOT NULL,
	[ContactLevel] [nvarchar](50) NULL,
	[Prefix] [char](10) NULL,
	[FirstName] [nvarchar](255) NULL,
	[MiddleName] [nvarchar](255) NULL,
	[LastName] [nvarchar](255) NULL,
	[Suffix] [char](10) NULL,
	[Email] [nvarchar](200) NULL,
	[Address1] [nvarchar](255) NULL,
	[AptSteFlr] [char](10) NULL,
	[Address2] [nvarchar](255) NULL,
	[City] [nvarchar](75) NULL,
	[County] [nvarchar](75) NULL,
	[StateProvince] [nvarchar](75) NULL,
	[ZipCode] [nvarchar](15) NULL,
	[Country] [nvarchar](75) NULL,
	[IsBillingContact] [bit] NULL,
	[IsAdminContact] [bit] NULL,
	[IsSignatoryContact] [bit] NULL,
	[SourceCreatedBy] [nvarchar](50) NULL,
	[SourceCreatedDate] [datetime] NULL,
	[SourceUpdatedBy] [nvarchar](50) NULL,
	[SourceUpdatedDate] [datetime] NULL,
	[CreatedBy] [nvarchar](50) NULL,
	[CreatedDate] [datetime] NULL,
	[UpdatedBy] [nvarchar](50) NULL,
	[UpdatedDate] [datetime] NULL,
PRIMARY KEY CLUSTERED 
(
	[ContactId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[LegalResource]    Script Date: 5/23/2022 5:47:36 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[LegalResource](
	[LegalResourceId] [bigint] IDENTITY(1,1) NOT NULL,
	[LegalResourceXref] [nvarchar](50) NULL,
	[EmployeeId] [nvarchar](50) NOT NULL,
	[FirmName] [nvarchar](255) NULL,
	[IsActive] [bit] NULL,
	[Prefix] [char](10) NULL,
	[FirstName] [nvarchar](255) NULL,
	[MiddleName] [nvarchar](255) NULL,
	[LastName] [nvarchar](255) NULL,
	[LegalResourceType] [nvarchar](50) NULL,
	[LegalResourceRole] [nvarchar](50) NULL,
	[BarNumber] [nvarchar](50) NULL,
	[LicensingAuthority] [nvarchar](50) NULL,
	[CaseWorkTime] [int] NULL,
	[Team] [nvarchar](50) NULL,
	[OfficeLocationCity] [nvarchar](75) NULL,
	[OfficeLocationStateProvince] [nvarchar](75) NULL,
	[OfficeLocationCountry] [nvarchar](75) NULL,
	[Address1] [nvarchar](255) NULL,
	[AptSteFlr] [char](10) NULL,
	[Address2] [nvarchar](255) NULL,
	[AddressType] [nvarchar](max) NULL,
	[AddressTypeNumber] [nvarchar](max) NULL,
	[City] [nvarchar](75) NULL,
	[County] [nvarchar](75) NULL,
	[StateProvince] [nvarchar](75) NULL,
	[ZipCode] [nvarchar](15) NULL,
	[Country] [nvarchar](75) NULL,
	[PhoneNumber] [nvarchar](75) NULL,
	[PhoneNumberExt] [char](10) NULL,
	[MobileNumber] [nvarchar](75) NULL,
	[FaxNumber] [nvarchar](15) NULL,
	[Email] [nvarchar](200) NULL,
	[SourceCreatedBy] [nvarchar](50) NULL,
	[SourceCreatedDate] [datetime] NULL,
	[SourceUpdatedBy] [nvarchar](50) NULL,
	[SourceUpdatedDate] [datetime] NULL,
	[CreatedBy] [nvarchar](50) NULL,
	[CreatedDate] [datetime] NULL,
	[UpdatedBy] [nvarchar](50) NULL,
	[UpdatedDate] [datetime] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Organization]    Script Date: 5/23/2022 5:47:36 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Organization](
	[OrganizationId] [bigint] IDENTITY(1,1) NOT NULL,
	[OrganizationXref] [nvarchar](255) NOT NULL,
	[OpenDate] [datetime] NULL,
	[IsActive] [bit] NULL,
	[InactiveDate] [datetime] NULL,
	[FirmClientNumber] [nvarchar](50) NULL,
	[OrganizationName] [nvarchar](255) NULL,
	[OrganizationShortName] [nvarchar](255) NULL,
	[TradeDBAName] [nvarchar](255) NULL,
	[YearEstablished] [nvarchar](50) NULL,
	[BusinessType] [nvarchar](150) NULL,
	[BusinessInfo] [nvarchar](max) NULL,
	[IndustryInfo] [nvarchar](150) NULL,
	[USEmployeeCount] [int] NULL,
	[WorldwideEmployeeCount] [int] NULL,
	[GrossAnnualIncome] [int] NULL,
	[NetAnnualIncome] [int] NULL,
	[FederalEmployerId] [nvarchar](15) NULL,
	[NaicsCode] [nvarchar](15) NULL,
	[BlanketLApprovalNumber] [nvarchar](20) NULL,
	[BlanketLExpirationDate] [datetime] NULL,
	[OriginatingAttorney] [nvarchar](255) NULL,
	[OriginatingAttorneyCredit] [int] NULL,
	[ManagingAttorney] [nvarchar](255) NULL,
	[ManagingAttorneyCredit] [int] NULL,
	[Address1] [nvarchar](255) NULL,
	[AptSteFlr] [char](10) NULL,
	[Address2] [nvarchar](255) NULL,
	[City] [nvarchar](75) NULL,
	[County] [nvarchar](75) NULL,
	[StateProvince] [nvarchar](75) NULL,
	[ZipCode] [nvarchar](15) NULL,
	[Country] [nvarchar](75) NULL,
	[PhoneNumber1] [nvarchar](15) NULL,
	[PhoneNumber1Ext] [char](10) NULL,
	[PhoneNumber2] [nvarchar](15) NULL,
	[PhoneNumber2Ext] [char](10) NULL,
	[MobileNumber] [nvarchar](15) NULL,
	[FaxNumber] [nvarchar](15) NULL,
	[ImmigrationBudgetCurrentYear] [int] NULL,
	[ImmigrationSpendCurrentYear] [int] NULL,
	[ImmigrationBudgetPreviousYear1] [int] NULL,
	[ImmigrationSpendPreviousYear1] [int] NULL,
	[ImmigrationBudgetPreviousYear2] [int] NULL,
	[ImmigrationSpendPreviousYear2] [int] NULL,
	[SourceCreatedBy] [nvarchar](50) NULL,
	[SourceCreatedDate] [datetime] NULL,
	[SourceUpdatedBy] [nvarchar](50) NULL,
	[SourceUpdatedDate] [datetime] NULL,
	[CreatedBy] [nvarchar](50) NULL,
	[CreatedDate] [datetime] NULL,
	[UpdatedBy] [nvarchar](50) NULL,
	[UpdatedDate] [datetime] NULL,
 CONSTRAINT [PK__Organiza__CADB0B123FFE6FD4] PRIMARY KEY CLUSTERED 
(
	[OrganizationId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Petitioner]    Script Date: 5/23/2022 5:47:36 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Petitioner](
	[PetitionerId] [bigint] IDENTITY(1,1) NOT NULL,
	[PetitionerXref] [nvarchar](50) NOT NULL,
	[OrganizationId] [bigint] NULL,
	[OpenedDate] [datetime] NULL,
	[IsActive] [bit] NULL,
	[InactiveDate] [datetime] NULL,
	[FirmClientNumber] [nvarchar](50) NULL,
	[PetitionerName] [nvarchar](255) NULL,
	[PetitionerShortName] [nvarchar](255) NULL,
	[PetitionerNameOnForm] [nvarchar](255) NULL,
	[PetitionerEmail] [nvarchar](200) NULL,
	[TradeDBAName] [nvarchar](255) NULL,
	[YearEstablished] [int] NULL,
	[BusinessType] [nvarchar](150) NULL,
	[BusinessInfo] [nvarchar](max) NULL,
	[IndustryType] [nvarchar](150) NULL,
	[USEmployeeCount] [int] NULL,
	[WorldwideEmployeeCount] [int] NULL,
	[GrossAnnualIncome] [nvarchar](200) NULL,
	[NetAnnualIncome] [nvarchar](200) NULL,
	[BlanketLApprovalNumber] [nvarchar](20) NULL,
	[BlanketLExpirationDate] [datetime] NULL,
	[IsPetitionerOnBlanketL] [bit] NULL,
	[IsPetitionerH1bDependent] [bit] NULL,
	[IsPetitionerWillfulViolator] [bit] NULL,
	[IsOver50PctEEH1bL1aL1bStatus] [bit] NULL,
	[IsHigherEducationInstitution] [bit] NULL,
	[IsNonprofitOrganizationEntity] [bit] NULL,
	[IsNonprofitGovernmentResearch] [bit] NULL,
	[IsPrimarySecondaryEducationInstitution] [bit] NULL,
	[IsNonprofitCurriculumRelatedTraining] [bit] NULL,
	[IsPetitionerGuamCnmiCapExempt] [bit] NULL,
	[FederalEmployerId] [nvarchar](15) NULL,
	[NaicsCode] [nvarchar](15) NULL,
	[Address1] [nvarchar](255) NULL,
	[AptSteFlr] [char](10) NULL,
	[Address2] [nvarchar](255) NULL,
	[City] [nvarchar](75) NULL,
	[County] [nvarchar](75) NULL,
	[StateProvince] [nvarchar](75) NULL,
	[ZipCode] [nvarchar](15) NULL,
	[Country] [nvarchar](75) NULL,
	[PhoneNumber1] [nvarchar](15) NULL,
	[PhoneNumber1Ext] [char](10) NULL,
	[PhoneNumber2] [nvarchar](15) NULL,
	[PhoneNumber2Ext] [char](10) NULL,
	[MobileNumber] [nvarchar](15) NULL,
	[FaxNumber] [nvarchar](15) NULL,
	[OriginatingAttorney] [nvarchar](255) NULL,
	[OriginatingAttorneyCredit] [int] NULL,
	[ManagingAttorney] [nvarchar](255) NULL,
	[ManagingAttorneyCredit] [int] NULL,
	[WorkingAttorney] [nvarchar](255) NULL,
	[WorkingAttorneyCredit] [int] NULL,
	[SourceCreatedBy] [nvarchar](50) NULL,
	[SourceCreatedDate] [datetime] NULL,
	[SourceUpdatedBy] [nvarchar](50) NULL,
	[SourceUpdatedDate] [datetime] NULL,
	[CreatedBy] [nvarchar](50) NULL,
	[CreatedDate] [datetime] NULL,
	[UpdatedBy] [nvarchar](50) NULL,
	[UpdatedDate] [datetime] NULL,
 CONSTRAINT [PK__Petition__178BDCF09C3D0DE2] PRIMARY KEY CLUSTERED 
(
	[PetitionerId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[PetitionerAuthorizedSignatory]    Script Date: 5/23/2022 5:47:36 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[PetitionerAuthorizedSignatory](
	[SignatoryId] [bigint] IDENTITY(1,1) NOT NULL,
	[PetitionerId] [bigint] NOT NULL,
	[SignatoryType] [nvarchar](max) NULL,
	[LastName] [nvarchar](max) NULL,
	[FirstName] [nvarchar](max) NULL,
	[MiddleName] [nvarchar](max) NULL,
	[Address1] [nvarchar](max) NULL,
	[AddressType] [nvarchar](max) NULL,
	[AddressTypeNumber] [nvarchar](max) NULL,
	[City] [nvarchar](max) NULL,
	[State] [nvarchar](max) NULL,
	[ZipCode] [nvarchar](max) NULL,
	[Country] [nvarchar](max) NULL,
	[JobTitle] [nvarchar](max) NULL,
	[PhoneNumber] [nvarchar](max) NULL,
	[MobilePhone] [nvarchar](max) NULL,
	[Email] [nvarchar](max) NULL,
 CONSTRAINT [PK_PetitionerAuthorizedSignatory] PRIMARY KEY CLUSTERED 
(
	[SignatoryId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[processed_form_details]    Script Date: 5/23/2022 5:47:36 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[processed_form_details](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[last_processed_form_id] [nvarchar](50) NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[VisaBulletinData]    Script Date: 5/23/2022 5:47:36 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[VisaBulletinData](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[VisaBulletinId] [int] NOT NULL,
	[col1] [text] NULL,
	[col2] [text] NULL,
	[col3] [text] NULL,
	[col4] [text] NULL,
	[col5] [text] NULL,
	[col6] [text] NULL,
	[col7] [text] NULL,
	[table_info] [nchar](10) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[VisaBulletinHeader]    Script Date: 5/23/2022 5:47:36 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[VisaBulletinHeader](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[month] [nvarchar](50) NULL,
	[year] [int] NULL,
	[text] [text] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
SET IDENTITY_INSERT [dbo].[Beneficiary] ON 

INSERT [dbo].[Beneficiary] ([BeneficiaryId], [BeneficiaryXref], [OrganizationId], [PetitionerId], [PrimaryBeneficiaryXref], [PrimaryBeneficiaryLastName], [PrimaryBeneficiaryFirstName], [CitizenshipCountry], [RelationType], [IsActive], [InactiveDate], [FirmClientNumber], [BeneficiaryType], [Prefix], [FirstName], [MiddleName], [LastName], [Suffix], [OtherFirstName], [OtherMiddleName], [OtherLastName], [WorkEmail], [PersonalEmail], [HomePhone], [WorkPhone], [Mobile], [IsRovingEmployee], [IsWorkOffsite], [IsWorkAtMultipleSites], [Gender], [SsnNumber], [AlienNumber], [BirthDate], [BirthCity], [BirthStateProvince], [BirthCountry], [MaritalStatus], [SpouseBirthCountry], [IsInRemovalProceeding], [MostRecentUSEntryDate], [MostRecentUSEntryCity], [MostRecentUSEntryState], [HasMostRecentUSEntryAdmitted], [MostRecentUSDepartureDate], [I94FirstName], [I94MiddleName], [I94LastName], [I94Number], [I94Status], [I94ValidFromDate], [I94ExpirationDate], [MostRecentUSI94EntryStatus], [MostRecentI797Status], [MostRecentI797ValidFromDate], [MaxOutDateNote], [I797ExpirationDate], [I797ReceiptNumber], [MostRecentI797IssueApprovalDate], [InitialHlEntryDate], [FinalNivDate], [FifthYearEndDate], [EndorsedI129sExpirationDate], [FormI129sRequestedExpirationDate], [VisaPedDate], [VisaIssueApprovalDate], [VisaCategory], [VisaType], [VisaValidFromDate], [VisaExpirationDate], [PassportFirstName], [PassportMiddleName], [PassportLastName], [PassportNumber], [PassportCountry], [PassportIssuedInCountry], [PassportIssueApprovalDate], [PassportValidFromDate], [PassportExpirationDate], [MostRecentI94EntryPassportNumber], [SevisNumber], [CPTValidFromDate], [CPTExpirationDate], [F1OptValidFromDate], [F1OptExpirationDate], [IsStemEligible], [F1StemOptValidFromDate], [F1StemOptExpirationDate], [HasPreviouslyHeldF1Status], [EadType], [EadNumber], [EadValidFromDate], [EadExpirationDate], [I140FileByDate], [AdvanceParoleValidFromDate], [AdvanceParoleExpirationDate], [EadApValidFromDate], [EadApExpirationDate], [GreenCardValidFromDate], [GreenCardExpirationDate], [ReEntryPermitValidFromDate], [ReEntryPermitExpirationDate], [I90FilingEligibilityDate], [I751FilingEligibilityDate], [N400FilingEligibilityDate], [HasPreviouslyHeldJVisaStatus], [PreviouslyHeldJVisaType], [JVisaType], [JVisaStatusValidFromDate], [JVisaStatusExpirationDate], [Ds2019IssueApprovalDate], [Ds2019ValidFromDate], [Ds2019ExpirationDate], [HasHomeStayRequirement], [HasHomeStayRequirementWaiverReceived], [PrProcessActualStartDate], [PrProcessTargetStartDate], [HasPrProcessInitiated], [PermCaseFiledDate], [PermCaseApprovedDate], [PermPriorityDate], [PermPriorityCategory], [PermPriorityCountry], [PermEta9089ExpirationDate], [I140CaseFiledDate], [I140CaseApprovedDate], [I140PetitionerName], [I140PriorityDate], [I140PriorityCategory], [I140PriorityCountry], [HasPriorEmployerApprovedI140], [PriorEmployerI140PetitionerName], [PriorEmployerI140PriorityDate], [PriorEmployerI140PriorityCategory], [PriorEmployerI140PriorityCountry], [AosCaseFiledDate], [AosCaseApprovedDate], [ManagingAttorney], [TravelDocumentIssueCountry], [MostRecentUSEntryTravelDocumentNumber], [NonimmigrantVisaNumber], [Ethnicity], [Race], [HeightFeet], [HeightInches], [EyeColor], [HairColor], [WeightLbs], [ImmigrationStatusValidFromDate], [ImmigrationStatusExpirationDate], [MostRecentPassportLastName], [MostRecentPassportFirstName], [MostRecentPassportNumber], [MostRecentPassportIssuingCountry], [MostRecentPassportMiddleName], [MostRecentPassportValidFromDate], [EADAPType], [MostRecentPassportExpirationDate], [ImmigrationStatus], [WeightKg], [SourceCreatedBy], [SourceCreatedDate], [SourceUpdatedBy], [SourceUpdatedDate], [CreatedBy], [CreatedDate], [UpdatedBy], [UpdatedDate], [from_name], [is_primary_beneficiary]) VALUES (1, N'BXREF002', NULL, 1, NULL, NULL, NULL, N'India', NULL, NULL, NULL, NULL, NULL, NULL, N'Gyanadeep', N'', N'Kankanala', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, N'100-01-0002', N'138124306.0', CAST(N'1990-10-03T00:00:00.000' AS DateTime), N'Franklin', N'TN', N'United States of America', NULL, NULL, NULL, CAST(N'2021-12-10T00:00:00.000' AS DateTime), NULL, NULL, NULL, NULL, NULL, NULL, NULL, N'123456789B1', N'H-1B', NULL, CAST(N'2024-01-31T00:00:00.000' AS DateTime), NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, N'B100001', N'India', NULL, NULL, NULL, CAST(N'2027-12-10T00:00:00.000' AS DateTime), NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1)
SET IDENTITY_INSERT [dbo].[Beneficiary] OFF
GO
SET IDENTITY_INSERT [dbo].[BeneficiaryAddress] ON 

INSERT [dbo].[BeneficiaryAddress] ([BeneficiaryAddressId], [BeneficiaryId], [AddressCountry], [AddressType], [AddressUnitType], [Address1], [AptSteFlr], [Address2], [City], [County], [StateProvince], [ZipCode], [Country], [AddressFromDate], [AddressToDate], [IsLastResidenceAbroad], [SourceCreatedBy], [SourceCreatedDate], [SourceUpdatedBy], [SourceUpdatedDate], [CreatedBy], [CreatedDate], [UpdatedBy], [UpdatedDate]) VALUES (1, 2, NULL, N'', N'', N'18302 Crowne Brook Circle', NULL, NULL, N'Franklin', NULL, N'TN', N'37067.0', N'United States of America', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)
INSERT [dbo].[BeneficiaryAddress] ([BeneficiaryAddressId], [BeneficiaryId], [AddressCountry], [AddressType], [AddressUnitType], [Address1], [AptSteFlr], [Address2], [City], [County], [StateProvince], [ZipCode], [Country], [AddressFromDate], [AddressToDate], [IsLastResidenceAbroad], [SourceCreatedBy], [SourceCreatedDate], [SourceUpdatedBy], [SourceUpdatedDate], [CreatedBy], [CreatedDate], [UpdatedBy], [UpdatedDate]) VALUES (2, 1, NULL, N'', N'', N'18302 Crowne Brook Circle', NULL, NULL, N'Franklin', NULL, N'TN', N'37067.0', N'United States of America', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)
INSERT [dbo].[BeneficiaryAddress] ([BeneficiaryAddressId], [BeneficiaryId], [AddressCountry], [AddressType], [AddressUnitType], [Address1], [AptSteFlr], [Address2], [City], [County], [StateProvince], [ZipCode], [Country], [AddressFromDate], [AddressToDate], [IsLastResidenceAbroad], [SourceCreatedBy], [SourceCreatedDate], [SourceUpdatedBy], [SourceUpdatedDate], [CreatedBy], [CreatedDate], [UpdatedBy], [UpdatedDate]) VALUES (3, 4, NULL, N'1A', N'Apt', N'444 Saratoga Ave.', NULL, NULL, N'Santa Clara', NULL, N'CA', N'95050.0', N'United States of America', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)
INSERT [dbo].[BeneficiaryAddress] ([BeneficiaryAddressId], [BeneficiaryId], [AddressCountry], [AddressType], [AddressUnitType], [Address1], [AptSteFlr], [Address2], [City], [County], [StateProvince], [ZipCode], [Country], [AddressFromDate], [AddressToDate], [IsLastResidenceAbroad], [SourceCreatedBy], [SourceCreatedDate], [SourceUpdatedBy], [SourceUpdatedDate], [CreatedBy], [CreatedDate], [UpdatedBy], [UpdatedDate]) VALUES (4, 3, NULL, N'A-15', N'Apt', N'2500 Test Drive', NULL, NULL, N'Auburn Hills', NULL, N'MI', N'48326.0', N'United States of America', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)
SET IDENTITY_INSERT [dbo].[BeneficiaryAddress] OFF
GO
SET IDENTITY_INSERT [dbo].[Case] ON 

INSERT [dbo].[Case] ([CaseId], [CaseXref], [OrganizationId], [BeneficiaryId], [CaseType], [RFEAuditDueDate], [RFEAuditSubmittedDate], [RFEAuditReceivedDate], [CasePetitionName], [PetitionerSponsorId], [ServiceType], [OriginatingCountry], [DestinationCountry], [CaseDescription], [CaseOpenDate], [IsPPEligibleAtFiling], [HasFiledByPP], [PPType], [CaseFiledDate], [ReceiptDateReceivedByGovt], [ReceiptNumber], [ReceiptStatus], [CaseApprovedDate], [CaseValidFromDate], [CaseExpirationDate], [PriorityDate], [PriorityCategory], [PriorityCountry], [PetitionXref], [CasePrimaryCaseManager], [CasePrimaryAttorney], [CaseReviewingAttorney], [CaseWithdrawnDate], [CaseClosedDate], [CaseDeniedDate], [DenialReason], [CaseComments], [PrimaryCaseStatus], [SecondaryCaseStatus], [SecondaryCaseStatusDate], [LastStepCompleted], [LastStepCompletedDate], [NextStepAction], [NextStepActionDueDate], [NextStepActionToBeTakenBy], [NotesInternal], [NotesExternal], [NotesConfidential], [AttorneyPrimaryIdXref], [AttorneyPrimaryEMPId], [AttorneyPrimaryFirstName], [AttorneyPrimaryMiddleName], [AttorneyPrimaryLastName], [AttorneyPrimaryCaseCreditPercentage], [Attorney2IdXref], [Attorney2EMPId], [Attorney2FirstName], [Attorney2MiddleName], [Attorney2LastName], [CaseWorkerPrimaryCaseCreditPercentage], [CaseWorkerPrimaryIdXref], [CaseWorkerPrimaryEMPId], [CaseWorkerPrimaryFirstName], [CaseWorkerPrimaryMiddleName], [CaseWorkerPrimaryLastName], [CaseWorker2CaseCreditPercentage], [CaseWorker2IdXref], [CaseWorker2EMPId], [CaseWorker2FirstName], [CaseWorker2MiddleName], [CaseWorker2LastName], [CaseWorker3CaseCreditPercentage], [CaseWorker3IdXref], [CaseWorker3EMPId], [CaseWorker3FirstName], [CaseWorker3MiddleName], [CaseWorker3LastName], [CaseInitiationDate], [AllDocsReceivedDate], [HrbpId], [HrbpFirstName], [HrbpMiddleName], [HrbpLastName], [HrbpEmail], [SupervisorManagerId], [SupervisorManagerFirstName], [SupervisorManagerMiddleName], [SupervisorManagerLastName], [SupervisorManagerEmail], [DepartmentCode], [DepartmentName], [BusinessUnit], [CostCenterCode], [CostCenterCodeName], [ProjectCode], [ProjectName], [SourceCreatedBy], [SourceCreatedDate], [SourceUpdatedBy], [SourceUpdatedDate], [CreatedBy], [CreatedDate], [UpdatedBy], [UpdatedDate], [from_name]) VALUES (1, N'CASEID0002', NULL, 1, NULL, NULL, NULL, NULL, N'i140', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, N'A2120220438', NULL, NULL, NULL, NULL, NULL, N'EB-3', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, N'100001', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)
SET IDENTITY_INSERT [dbo].[Case] OFF
GO
SET IDENTITY_INSERT [dbo].[ClientDetails] ON 

INSERT [dbo].[ClientDetails] ([id], [client_name], [clientShortName], [organizationName], [organizationXref], [petitionerName], [petitionerXref], [report_name], [cadence], [delivery_day], [delivery_time], [recipient_to], [recipient_cc], [no_of_tabs], [special_criteria], [expiration_report_sent], [expiration_report_sent_on], [status_report_sent_on]) VALUES (1, N'Abercrombie & Fitch', N'A&F', N'Abercrombie & Fitch Management Co.', N'HGEYM07803', NULL, NULL, N'Status Report', N'Weekly', N'Monday', N'11:00', N'thompsonmir@gtlaw.com;', N'', 6, N'No        ', 0, NULL, NULL)
INSERT [dbo].[ClientDetails] ([id], [client_name], [clientShortName], [organizationName], [organizationXref], [petitionerName], [petitionerXref], [report_name], [cadence], [delivery_day], [delivery_time], [recipient_to], [recipient_cc], [no_of_tabs], [special_criteria], [expiration_report_sent], [expiration_report_sent_on], [status_report_sent_on]) VALUES (2, N'Acuity Lighting Brands', N'Acuity', N'Acuity', N'HGEYM23236', NULL, NULL, N'Status Report', N'Weekly', N'Monday', N'10:00', N'Acuity@gtlaw.com', N'', 6, N'Yes       ', 0, NULL, NULL)
INSERT [dbo].[ClientDetails] ([id], [client_name], [clientShortName], [organizationName], [organizationXref], [petitionerName], [petitionerXref], [report_name], [cadence], [delivery_day], [delivery_time], [recipient_to], [recipient_cc], [no_of_tabs], [special_criteria], [expiration_report_sent], [expiration_report_sent_on], [status_report_sent_on]) VALUES (3, N'Aggreko', N'Aggreko', N'Aggreko, LLC', N'HGEYM45061', NULL, NULL, N'Status Report', N'Weekly', N'Tuesday', N'10:00', N'Aggrekoimmigration@gtlaw.com', N'', 6, N'No        ', 0, NULL, NULL)
INSERT [dbo].[ClientDetails] ([id], [client_name], [clientShortName], [organizationName], [organizationXref], [petitionerName], [petitionerXref], [report_name], [cadence], [delivery_day], [delivery_time], [recipient_to], [recipient_cc], [no_of_tabs], [special_criteria], [expiration_report_sent], [expiration_report_sent_on], [status_report_sent_on]) VALUES (4, N'Alcon', N'Alcon', N'Alcon Laboratories, Inc.', N'HGEYM07812', NULL, NULL, N'Status Report', N'Weekly', N'Tuesday', N'10:00', N'heyerc@gtlaw.com;macdonaldi@gtlaw.com;vicenten@gtlaw.com;', N'', 6, N'No        ', 0, NULL, NULL)
INSERT [dbo].[ClientDetails] ([id], [client_name], [clientShortName], [organizationName], [organizationXref], [petitionerName], [petitionerXref], [report_name], [cadence], [delivery_day], [delivery_time], [recipient_to], [recipient_cc], [no_of_tabs], [special_criteria], [expiration_report_sent], [expiration_report_sent_on], [status_report_sent_on]) VALUES (5, N'Ascena', N'Ascena', N'Ascena Retail Group', N'HGEYM07810', NULL, NULL, N'Status Report', N'Weekly', N'', N'11:00', N'heyerc@gtlaw.com', N'SantiestebanA@gtlaw.com;', 6, N'TBD       ', 0, NULL, NULL)
INSERT [dbo].[ClientDetails] ([id], [client_name], [clientShortName], [organizationName], [organizationXref], [petitionerName], [petitionerXref], [report_name], [cadence], [delivery_day], [delivery_time], [recipient_to], [recipient_cc], [no_of_tabs], [special_criteria], [expiration_report_sent], [expiration_report_sent_on], [status_report_sent_on]) VALUES (6, N'Bacardi', N'Bacardi', N'Bacardi U.S.A., Inc.', N'HGEYM07811', NULL, NULL, N'Status Report', N'Weekly', N'Tuesday', N'11:00', N'CappellariC@gtlaw.com;', N'nocec@gtlaw.com;', 6, N'Yes       ', 0, NULL, NULL)
INSERT [dbo].[ClientDetails] ([id], [client_name], [clientShortName], [organizationName], [organizationXref], [petitionerName], [petitionerXref], [report_name], [cadence], [delivery_day], [delivery_time], [recipient_to], [recipient_cc], [no_of_tabs], [special_criteria], [expiration_report_sent], [expiration_report_sent_on], [status_report_sent_on]) VALUES (7, N'BSCA', N'BSCA', N'Blue Shield of California', N'HGEYM45067', NULL, NULL, N'Status Report', N'Weekly', N'Thursday', N'10:00', N'BSCAimmigration@gtlaw.com', N'', 6, N'No        ', 0, NULL, NULL)
INSERT [dbo].[ClientDetails] ([id], [client_name], [clientShortName], [organizationName], [organizationXref], [petitionerName], [petitionerXref], [report_name], [cadence], [delivery_day], [delivery_time], [recipient_to], [recipient_cc], [no_of_tabs], [special_criteria], [expiration_report_sent], [expiration_report_sent_on], [status_report_sent_on]) VALUES (8, N'Campbells Soups', N'Campbells Soup', N'Campbells Soup', N'HGEYM31083', NULL, NULL, N'Status Report', N'Weekly', N'Tuesday', N'12:00', N'thompsonmir@gtlaw.com;', N'nocec@gtlaw.com;', 6, N'No        ', 0, NULL, NULL)
INSERT [dbo].[ClientDetails] ([id], [client_name], [clientShortName], [organizationName], [organizationXref], [petitionerName], [petitionerXref], [report_name], [cadence], [delivery_day], [delivery_time], [recipient_to], [recipient_cc], [no_of_tabs], [special_criteria], [expiration_report_sent], [expiration_report_sent_on], [status_report_sent_on]) VALUES (9, N'Coca-Cola', N'Coca-Cola', N'Coca-Cola Refreshments USA, Inc.', N'HGEYM02955', NULL, NULL, N'Status Report', N'Bi-Weekly', N'Wednesday', N'10:00', N'heyerc@gtlaw.com;', N'graya@gtlaw.com;', 6, N'No        ', 0, NULL, NULL)
INSERT [dbo].[ClientDetails] ([id], [client_name], [clientShortName], [organizationName], [organizationXref], [petitionerName], [petitionerXref], [report_name], [cadence], [delivery_day], [delivery_time], [recipient_to], [recipient_cc], [no_of_tabs], [special_criteria], [expiration_report_sent], [expiration_report_sent_on], [status_report_sent_on]) VALUES (10, N'Copart', N'Copart', N'', N'', N'Copart, Inc. ', N'PJU24902', N'Status Report', N'Weekly', N'', N'10:00', N'nocec@gtlaw.com;', N'graya@gtlaw.com;', 6, N'TBD       ', 0, NULL, NULL)
INSERT [dbo].[ClientDetails] ([id], [client_name], [clientShortName], [organizationName], [organizationXref], [petitionerName], [petitionerXref], [report_name], [cadence], [delivery_day], [delivery_time], [recipient_to], [recipient_cc], [no_of_tabs], [special_criteria], [expiration_report_sent], [expiration_report_sent_on], [status_report_sent_on]) VALUES (11, N'Del Monte', N'Del Monte', N'Del Monte', N'HGEYM37764', NULL, NULL, N'Status Report', N'Weekly', N'Thursday', N'11:00', N'heyerc@gtlaw.com', N'holodj@gtlaw.com', 6, N'No        ', 0, NULL, NULL)
INSERT [dbo].[ClientDetails] ([id], [client_name], [clientShortName], [organizationName], [organizationXref], [petitionerName], [petitionerXref], [report_name], [cadence], [delivery_day], [delivery_time], [recipient_to], [recipient_cc], [no_of_tabs], [special_criteria], [expiration_report_sent], [expiration_report_sent_on], [status_report_sent_on]) VALUES (12, N'EDP & EDPR', N'EDP & EDPR', N'EDP', N'HGEYM40230', NULL, NULL, N'Status Report', N'Weekly', N'Monday', N'10:00', N'holodj@gtlaw.com', N'nocec@gtlaw.com;', 6, N'Yes       ', 0, NULL, NULL)
INSERT [dbo].[ClientDetails] ([id], [client_name], [clientShortName], [organizationName], [organizationXref], [petitionerName], [petitionerXref], [report_name], [cadence], [delivery_day], [delivery_time], [recipient_to], [recipient_cc], [no_of_tabs], [special_criteria], [expiration_report_sent], [expiration_report_sent_on], [status_report_sent_on]) VALUES (13, N'Euromonitor', N'Euromonitor', N'Euromonitor International, Inc.', N'HGEYM45070', NULL, NULL, N'Status Report', N'Weekly', N'Thursday', N'11:00', N'holodj@gtlaw.com', N'nocec@gtlaw.com;', 6, N'No        ', 0, NULL, NULL)
INSERT [dbo].[ClientDetails] ([id], [client_name], [clientShortName], [organizationName], [organizationXref], [petitionerName], [petitionerXref], [report_name], [cadence], [delivery_day], [delivery_time], [recipient_to], [recipient_cc], [no_of_tabs], [special_criteria], [expiration_report_sent], [expiration_report_sent_on], [status_report_sent_on]) VALUES (14, N'Express', N'Express', N'Express, LLC', N'HGEYM45069', NULL, NULL, N'Status Report', N'Weekly', N'Thursday', N'11:00', N'nocec@gtlaw.com;thompsonmir@gtlaw.com;', N'', 6, N'No        ', 0, NULL, NULL)
INSERT [dbo].[ClientDetails] ([id], [client_name], [clientShortName], [organizationName], [organizationXref], [petitionerName], [petitionerXref], [report_name], [cadence], [delivery_day], [delivery_time], [recipient_to], [recipient_cc], [no_of_tabs], [special_criteria], [expiration_report_sent], [expiration_report_sent_on], [status_report_sent_on]) VALUES (15, N'Fractal', N'Fractal', N'Fractal Analytics, Inc.', N'HGEYM45063', NULL, NULL, N'Status Report', N'Weekly', N'Tuesday', N'13:00', N'Fractal@gtlaw.com;', N'', 6, N'No        ', 0, NULL, NULL)
INSERT [dbo].[ClientDetails] ([id], [client_name], [clientShortName], [organizationName], [organizationXref], [petitionerName], [petitionerXref], [report_name], [cadence], [delivery_day], [delivery_time], [recipient_to], [recipient_cc], [no_of_tabs], [special_criteria], [expiration_report_sent], [expiration_report_sent_on], [status_report_sent_on]) VALUES (16, N'Lectra & Gerber', N'Lectra & Gerber', N'Lectra', N'HGEYM41224', NULL, NULL, N'Status Report', N'Weekly', N'Thursday', N'11:00', N'holodj@gtlaw.com', N'', 6, N'No        ', 0, NULL, NULL)
INSERT [dbo].[ClientDetails] ([id], [client_name], [clientShortName], [organizationName], [organizationXref], [petitionerName], [petitionerXref], [report_name], [cadence], [delivery_day], [delivery_time], [recipient_to], [recipient_cc], [no_of_tabs], [special_criteria], [expiration_report_sent], [expiration_report_sent_on], [status_report_sent_on]) VALUES (17, N'LendingTree & QuoteWizard', N'LendingTree & QuoteWizard', N'LendingTree', N'HGEYM39412', NULL, NULL, N'Status Report', N'Weekly', N'Thursday', N'10:00', N'LTimmigration@gtlaw.com', N'', 6, N'No        ', 0, NULL, NULL)
INSERT [dbo].[ClientDetails] ([id], [client_name], [clientShortName], [organizationName], [organizationXref], [petitionerName], [petitionerXref], [report_name], [cadence], [delivery_day], [delivery_time], [recipient_to], [recipient_cc], [no_of_tabs], [special_criteria], [expiration_report_sent], [expiration_report_sent_on], [status_report_sent_on]) VALUES (18, N'Lidl', N'Lidl', N'Lidl', N'HGEYM14682', NULL, NULL, N'Status Report', N'Weekly', N'Thursday', N'11:00', N'nocec@gtlaw.com;
holodj@gtlaw.com', N'sawnn@gtlaw.com;burrelln@gtlaw.com', 6, N'No        ', 0, NULL, NULL)
INSERT [dbo].[ClientDetails] ([id], [client_name], [clientShortName], [organizationName], [organizationXref], [petitionerName], [petitionerXref], [report_name], [cadence], [delivery_day], [delivery_time], [recipient_to], [recipient_cc], [no_of_tabs], [special_criteria], [expiration_report_sent], [expiration_report_sent_on], [status_report_sent_on]) VALUES (19, N'OneMain', N'OneMain', N'Springleaf General Services Corporation', N'HGEYM09938', NULL, NULL, N'Status Report', N'Weekly', N'Thursday', N'10:00', N'porterl@gtlaw.com;', N'onemain@gtlaw.com;', 6, N'No        ', 0, NULL, NULL)
INSERT [dbo].[ClientDetails] ([id], [client_name], [clientShortName], [organizationName], [organizationXref], [petitionerName], [petitionerXref], [report_name], [cadence], [delivery_day], [delivery_time], [recipient_to], [recipient_cc], [no_of_tabs], [special_criteria], [expiration_report_sent], [expiration_report_sent_on], [status_report_sent_on]) VALUES (20, N'SCM', N'SCM', N'SCM Group North America, Inc.', N'HGEYM45071', NULL, NULL, N'Status Report', N'Bi-Weekly', N'Monday', N'10:00', N'holodj@gtlaw.com', N'', 6, N'No        ', 0, NULL, NULL)
INSERT [dbo].[ClientDetails] ([id], [client_name], [clientShortName], [organizationName], [organizationXref], [petitionerName], [petitionerXref], [report_name], [cadence], [delivery_day], [delivery_time], [recipient_to], [recipient_cc], [no_of_tabs], [special_criteria], [expiration_report_sent], [expiration_report_sent_on], [status_report_sent_on]) VALUES (21, N'SES', N'SES', N'SES', N'HGEYM32353', NULL, NULL, N'Status Report', N'Bi-Weekly', N'Thursday', N'10:00', N'holodj@gtlaw.com', N'', 6, N'No        ', 0, NULL, NULL)
INSERT [dbo].[ClientDetails] ([id], [client_name], [clientShortName], [organizationName], [organizationXref], [petitionerName], [petitionerXref], [report_name], [cadence], [delivery_day], [delivery_time], [recipient_to], [recipient_cc], [no_of_tabs], [special_criteria], [expiration_report_sent], [expiration_report_sent_on], [status_report_sent_on]) VALUES (22, N'Spirent & OctoScope', N'Spirent & OctoScope', N'Spirent', N'HGEYM38577', NULL, NULL, N'Status Report', N'Weekly', N'Tuesday', N'10:00', N'Spirentimmigration@gtlaw.com', N'', 6, N'No        ', 0, NULL, NULL)
INSERT [dbo].[ClientDetails] ([id], [client_name], [clientShortName], [organizationName], [organizationXref], [petitionerName], [petitionerXref], [report_name], [cadence], [delivery_day], [delivery_time], [recipient_to], [recipient_cc], [no_of_tabs], [special_criteria], [expiration_report_sent], [expiration_report_sent_on], [status_report_sent_on]) VALUES (23, N'Subway', N'Subway', N'Franchise World Headquarters, LLC', N'HGEYM45059', NULL, NULL, N'Status Report', N'Weekly', N'Monday', N'12:00', N'nocec@gtlaw.com;thompsonmir@gtlaw.com;', N'', 6, N'No        ', 0, NULL, NULL)
INSERT [dbo].[ClientDetails] ([id], [client_name], [clientShortName], [organizationName], [organizationXref], [petitionerName], [petitionerXref], [report_name], [cadence], [delivery_day], [delivery_time], [recipient_to], [recipient_cc], [no_of_tabs], [special_criteria], [expiration_report_sent], [expiration_report_sent_on], [status_report_sent_on]) VALUES (24, N'Symphony', N'Symphony', N'', N'', N'Symphony Communication Services LLC ', N'PGEYM36112', N'Status Report', N'Weekly', N'Wednesday', N'17:00', N'thompsonmir@gtlaw.com;', N'', 6, N'No        ', 0, NULL, NULL)
INSERT [dbo].[ClientDetails] ([id], [client_name], [clientShortName], [organizationName], [organizationXref], [petitionerName], [petitionerXref], [report_name], [cadence], [delivery_day], [delivery_time], [recipient_to], [recipient_cc], [no_of_tabs], [special_criteria], [expiration_report_sent], [expiration_report_sent_on], [status_report_sent_on]) VALUES (25, N'Tapestry', N'Tapestry', N'Tapestry', N'HGEYM15149', NULL, NULL, N'Status Report', N'Weekly', N'Tuesday', N'10:00', N'nocec@gtlaw.com;porterl@gtlaw.com;thompsonmir@gtlaw.com;', N'graya@gtlaw.com;', 6, N'No        ', 0, NULL, NULL)
INSERT [dbo].[ClientDetails] ([id], [client_name], [clientShortName], [organizationName], [organizationXref], [petitionerName], [petitionerXref], [report_name], [cadence], [delivery_day], [delivery_time], [recipient_to], [recipient_cc], [no_of_tabs], [special_criteria], [expiration_report_sent], [expiration_report_sent_on], [status_report_sent_on]) VALUES (26, N'Target', N'Target', N'Target Corporation', N'HGEYM08774', NULL, NULL, N'Status Report', N'Bi-Weekly', N'Wednesday', N'10:00', N'heyerc@gtlaw.com;', N'holodj@gtlaw.com; Target@gtlaw.com', 6, N'No        ', 0, NULL, NULL)
INSERT [dbo].[ClientDetails] ([id], [client_name], [clientShortName], [organizationName], [organizationXref], [petitionerName], [petitionerXref], [report_name], [cadence], [delivery_day], [delivery_time], [recipient_to], [recipient_cc], [no_of_tabs], [special_criteria], [expiration_report_sent], [expiration_report_sent_on], [status_report_sent_on]) VALUES (27, N'Zimmer', N'Zimmer', N'Zimmer HQ', N'HGEYM25599', NULL, NULL, N'Status Report', N'Weekly', N'Monday', N'11:00', N'rubyj@gtlaw.com;parkse@gtlaw.com', N'', 6, N'No        ', 0, NULL, NULL)
INSERT [dbo].[ClientDetails] ([id], [client_name], [clientShortName], [organizationName], [organizationXref], [petitionerName], [petitionerXref], [report_name], [cadence], [delivery_day], [delivery_time], [recipient_to], [recipient_cc], [no_of_tabs], [special_criteria], [expiration_report_sent], [expiration_report_sent_on], [status_report_sent_on]) VALUES (28, N'Zoom Video', N'Zoom Video', N'', N'', N'Zoom Video Communications, Inc.', N'PGEYM38352', N'Status Report', N'Weekly', N'Wednesday', N'12:00', N'holodj@gtlaw.com', N'graya@gtlaw.com;nocec@gtlaw.com;', 6, N'No        ', 0, NULL, NULL)
SET IDENTITY_INSERT [dbo].[ClientDetails] OFF
GO
SET IDENTITY_INSERT [dbo].[LegalResource] ON 

INSERT [dbo].[LegalResource] ([LegalResourceId], [LegalResourceXref], [EmployeeId], [FirmName], [IsActive], [Prefix], [FirstName], [MiddleName], [LastName], [LegalResourceType], [LegalResourceRole], [BarNumber], [LicensingAuthority], [CaseWorkTime], [Team], [OfficeLocationCity], [OfficeLocationStateProvince], [OfficeLocationCountry], [Address1], [AptSteFlr], [Address2], [AddressType], [AddressTypeNumber], [City], [County], [StateProvince], [ZipCode], [Country], [PhoneNumber], [PhoneNumberExt], [MobileNumber], [FaxNumber], [Email], [SourceCreatedBy], [SourceCreatedDate], [SourceUpdatedBy], [SourceUpdatedDate], [CreatedBy], [CreatedDate], [UpdatedBy], [UpdatedDate]) VALUES (1, N'', N'100001', N'Global Immigration Partners, Inc.', NULL, NULL, N'Richard', N'A', N'Harding', NULL, NULL, N'246801', NULL, NULL, NULL, NULL, NULL, NULL, N'30300 Agoura Rd.', NULL, NULL, N'Ste.', N'B-100', N'Agoura Hills', NULL, N'CA', N'91301', N'U.S.A.', N'818-914-6482', NULL, N'', NULL, N'rah@gip-us.com', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)
SET IDENTITY_INSERT [dbo].[LegalResource] OFF
GO
SET IDENTITY_INSERT [dbo].[Organization] ON 

INSERT [dbo].[Organization] ([OrganizationId], [OrganizationXref], [OpenDate], [IsActive], [InactiveDate], [FirmClientNumber], [OrganizationName], [OrganizationShortName], [TradeDBAName], [YearEstablished], [BusinessType], [BusinessInfo], [IndustryInfo], [USEmployeeCount], [WorldwideEmployeeCount], [GrossAnnualIncome], [NetAnnualIncome], [FederalEmployerId], [NaicsCode], [BlanketLApprovalNumber], [BlanketLExpirationDate], [OriginatingAttorney], [OriginatingAttorneyCredit], [ManagingAttorney], [ManagingAttorneyCredit], [Address1], [AptSteFlr], [Address2], [City], [County], [StateProvince], [ZipCode], [Country], [PhoneNumber1], [PhoneNumber1Ext], [PhoneNumber2], [PhoneNumber2Ext], [MobileNumber], [FaxNumber], [ImmigrationBudgetCurrentYear], [ImmigrationSpendCurrentYear], [ImmigrationBudgetPreviousYear1], [ImmigrationSpendPreviousYear1], [ImmigrationBudgetPreviousYear2], [ImmigrationSpendPreviousYear2], [SourceCreatedBy], [SourceCreatedDate], [SourceUpdatedBy], [SourceUpdatedDate], [CreatedBy], [CreatedDate], [UpdatedBy], [UpdatedDate]) VALUES (1, N'OXREF001', NULL, NULL, NULL, NULL, N'Evicor Healthcare', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)
SET IDENTITY_INSERT [dbo].[Organization] OFF
GO
SET IDENTITY_INSERT [dbo].[Petitioner] ON 

INSERT [dbo].[Petitioner] ([PetitionerId], [PetitionerXref], [OrganizationId], [OpenedDate], [IsActive], [InactiveDate], [FirmClientNumber], [PetitionerName], [PetitionerShortName], [PetitionerNameOnForm], [PetitionerEmail], [TradeDBAName], [YearEstablished], [BusinessType], [BusinessInfo], [IndustryType], [USEmployeeCount], [WorldwideEmployeeCount], [GrossAnnualIncome], [NetAnnualIncome], [BlanketLApprovalNumber], [BlanketLExpirationDate], [IsPetitionerOnBlanketL], [IsPetitionerH1bDependent], [IsPetitionerWillfulViolator], [IsOver50PctEEH1bL1aL1bStatus], [IsHigherEducationInstitution], [IsNonprofitOrganizationEntity], [IsNonprofitGovernmentResearch], [IsPrimarySecondaryEducationInstitution], [IsNonprofitCurriculumRelatedTraining], [IsPetitionerGuamCnmiCapExempt], [FederalEmployerId], [NaicsCode], [Address1], [AptSteFlr], [Address2], [City], [County], [StateProvince], [ZipCode], [Country], [PhoneNumber1], [PhoneNumber1Ext], [PhoneNumber2], [PhoneNumber2Ext], [MobileNumber], [FaxNumber], [OriginatingAttorney], [OriginatingAttorneyCredit], [ManagingAttorney], [ManagingAttorneyCredit], [WorkingAttorney], [WorkingAttorneyCredit], [SourceCreatedBy], [SourceCreatedDate], [SourceUpdatedBy], [SourceUpdatedDate], [CreatedBy], [CreatedDate], [UpdatedBy], [UpdatedDate]) VALUES (1, N'PXREF002', 1, NULL, NULL, NULL, NULL, N'Evicor Healthcare MSI', NULL, NULL, NULL, NULL, 1995, N'Software Services', NULL, NULL, 5000, NULL, N'$500 Million', N'$50 Million', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, N'621615395', N'5242', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)
SET IDENTITY_INSERT [dbo].[Petitioner] OFF
GO
SET IDENTITY_INSERT [dbo].[PetitionerAuthorizedSignatory] ON 

INSERT [dbo].[PetitionerAuthorizedSignatory] ([SignatoryId], [PetitionerId], [SignatoryType], [LastName], [FirstName], [MiddleName], [Address1], [AddressType], [AddressTypeNumber], [City], [State], [ZipCode], [Country], [JobTitle], [PhoneNumber], [MobilePhone], [Email]) VALUES (1, 1, NULL, N'Sansom', N'Tyler', N'', N'730 Cool Springs Boulvard', N'Suite', N'800.0', N'Franklin', N'TN', N'37067', N'United States of America', N'Immigration Manager', N'800-001-0002', N'800-001-0002', N'shiv@tesimmilytics.com')
SET IDENTITY_INSERT [dbo].[PetitionerAuthorizedSignatory] OFF
GO
SET IDENTITY_INSERT [dbo].[processed_form_details] ON 

INSERT [dbo].[processed_form_details] ([id], [last_processed_form_id]) VALUES (1, N'0')
SET IDENTITY_INSERT [dbo].[processed_form_details] OFF
GO
ALTER TABLE [dbo].[Beneficiary] ADD  CONSTRAINT [DF_Beneficiary_is_primary_beneficiary]  DEFAULT ((1)) FOR [is_primary_beneficiary]
GO
ALTER TABLE [dbo].[ClientDetails] ADD  CONSTRAINT [DF_ClientDetails_expiration_report_sent]  DEFAULT ((0)) FOR [expiration_report_sent]
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'US/Foreign' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'BeneficiaryAddress', @level2type=N'COLUMN',@level2name=N'AddressCountry'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Residence Address/ Work Address/ Mailing Address' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'BeneficiaryAddress', @level2type=N'COLUMN',@level2name=N'AddressType'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Flr/Street/Building' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'BeneficiaryAddress', @level2type=N'COLUMN',@level2name=N'AddressUnitType'
GO
USE [master]
GO
ALTER DATABASE [immilyticsi140] SET  READ_WRITE 
GO
