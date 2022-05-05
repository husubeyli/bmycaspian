from modeltranslation.translator import translator, TranslationOptions, register
from core.models import Navbar, \
    Addesses, Partners, \
    Products, \
    Projects, \
    Clients, \
    Service, \
    TeamMember, \
    News, \
    ProjectStatistics, \
    ProjectCategories, \
    StaticText, \
    WebsiteSettings, \
    SocialAccount, \
    AboutPageContent, \
    BulletPoint
    
    
    
    



class AboutPageContentTranslationOptions(TranslationOptions):
    fields = ('author_position',)


class NavbarTranslationOption(TranslationOptions):
    fields = (
        'title',
        'url',
    )

class BulletPointTranslationOptions(TranslationOptions):
    fields = ('title',)

class NavbarTranslationOption(TranslationOptions):
    fields = (
        'title',
        'url',
    )


class AddessesTranslationOption(TranslationOptions):
    fields = (
        'type_name',
        'full_address',
    )


class ProductsTranslationOption(TranslationOptions):
    fields = (
        'name',
        'description',
    )


class ProjectsTranslationOption(TranslationOptions):
    fields = (
        'title',
        'description',
    )


class ClientsTranslationOption(TranslationOptions):
    fields = (
        'title',
    )

class PartnersTranslationOption(TranslationOptions):
    fields = (
        'title',
    )


class ServiceTranslationOption(TranslationOptions):
    fields = (
        'title',
        'description',
    )


class TeamMemberTranslationOption(TranslationOptions):
    fields = (
        'name',
        'surname',
        'position',
    )


class NewsTranslationOption(TranslationOptions):
    fields = (
        'title',
        'description',
    )


class ProjectStatisticsTranslationOption(TranslationOptions):
    fields = (
        'name',
    )


class ProjectCategoriesTranslationOption(TranslationOptions):
    fields = (
        'title',
    )


class StaticTextTranslationOption(TranslationOptions):
    fields = (
        'surtitle',
        'title',
        'subtitle',
    )


class WebsiteSettingsTranslationOption(TranslationOptions):
    fields = (
        'company_name',
        'footer_text',
        'address',
    )


class SocialAccountTranslationOption(TranslationOptions):
    fields = (
        'teammember_name',
        'name',
    )


translator.register(BulletPoint, BulletPointTranslationOptions)
translator.register(AboutPageContent, AboutPageContentTranslationOptions)
translator.register(Navbar, NavbarTranslationOption)
translator.register(Addesses, AddessesTranslationOption)
translator.register(Products, ProductsTranslationOption)
translator.register(Projects, ProjectsTranslationOption)
translator.register(Clients, ClientsTranslationOption)
translator.register(Partners, PartnersTranslationOption)
translator.register(Service, ServiceTranslationOption)
translator.register(TeamMember, TeamMemberTranslationOption)
translator.register(News, NewsTranslationOption)
translator.register(ProjectStatistics, ProjectStatisticsTranslationOption)
translator.register(ProjectCategories, ProjectCategoriesTranslationOption)
translator.register(StaticText, StaticTextTranslationOption)
translator.register(WebsiteSettings, WebsiteSettingsTranslationOption)
translator.register(SocialAccount, SocialAccountTranslationOption)
