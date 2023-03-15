# %%
from manim import *


# %%
def playSpinner(self: Scene, duration: float = 4, scale: float = 1):
    circle = Circle(scale * 1/4).to_corner(RIGHT +
                                           DOWN).set_fill(None, 0).set_stroke(WHITE)

    self.add_foreground_mobject(circle)
    self.play(Create(circle, run_time=duration*3/4))
    self.play(Uncreate(circle.set_points(
        circle.get_all_points()[::-1]), run_time=duration*1/4))


def fadeAll(self: Scene, shift: np.ndarray = None):
    if len(self.mobjects) > 0:
        self.play(*[FadeOut(obj, shift=shift) for obj in self.mobjects])

# %%
#!%%manim -qm Intro


class Intro(Scene):
    def construct(self):
        title = MarkupText(
            'Problemas causados pelo <span>sedentarismo</span>', color=WHITE)
        title_red = MarkupText(
            f'Problemas causados pelo <span fgcolor="{RED}">sedentarismo</span>', color=WHITE)

        subtitle = VGroup(Text('O que é obesidade', font_size=DEFAULT_FONT_SIZE*3/4), Text(
            'e as estatisticas do mundo atual', font_size=DEFAULT_FONT_SIZE*3/4)).arrange(DOWN)

        VGroup(title, subtitle).arrange(DOWN, buff=1.5)

        title_red.move_to(title)

        self.add(title)
        self.wait(.75)
        self.play(Transform(title, title_red))
        self.play(Write(subtitle))
        playSpinner(self)
        fadeAll(self)

# %%
#!%%manim -qm ObesityDefinition


class ObesityDefinition(Scene):
    def construct(self):
        title = MarkupText("<b>Obesidade</b>:")
        definition = Paragraph("A obesidade é o acúmulo de gordura no corpo causado quase", "sempre por um consumo de energia na alimentação, superior", "àquela usada pelo organismo para sua manutenção e realização",
                               "das atividades do dia-a-dia. Ou seja: a ingestão alimentar é", "maior que o gasto energético correspondente.", font_size=DEFAULT_FONT_SIZE*3/5)
        diseases = Paragraph("Pessoas obesas têm maior probabilidade de desenvolver",
                             "doenças como pressão alta, diabetes, problemas nas", "articulações, dificuldades respiratórias, gota, pedras na vesícula", "e até algumas formas de câncer.", font_size=DEFAULT_FONT_SIZE*3/5)
        diagnostic = Paragraph("Uma pessoa está obesa quando o índice de massa corporal (IMC)",
                               "dela é de 30 ou mais.", font_size=DEFAULT_FONT_SIZE*3/5)
        texts = VGroup(definition, diseases, diagnostic).arrange(DOWN, center=False,
                                                                 aligned_edge=LEFT, buff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER*1.5)
        source = Text("Fonte: https://bvsms.saude.gov.br/obesidade-18/",
                      font_size=DEFAULT_FONT_SIZE*1/5).to_corner(LEFT + DOWN)
        VGroup(title, texts).arrange(DOWN, center=False,
                                     aligned_edge=LEFT).to_corner(LEFT + UP)
        self.play(AddTextLetterByLetter(title, run_time=1),
                  LaggedStart(*[FadeIn(text, shift=UP) for text in texts], run_time=3, lag_ratio=1/4))
        self.play(AddTextLetterByLetter(source, run_time=0.25))
        playSpinner(self)
        fadeAll(self)

# %%
#!%%manim -qm Statistics


class Statistics(Scene):
    def construct(self):
        title_number_of_adults = MarkupText(
            "<b>Numero de adultos obesos em 2016</b>").to_edge(UP)
        source_number_of_adults = Text("Fonte: https://www.who.int/news-room/fact-sheets/detail/obesity-and-overweight",
                                       font_size=DEFAULT_FONT_SIZE*1/5).to_corner(LEFT + DOWN)
        legend_number_of_adults = Text(
            "Milhões de pessoas", font_size=DEFAULT_FONT_SIZE*2/5)
        chart_number_of_adults = BarChart(
            values=[1900, 650],
            bar_names=["Sobrepeso", "Obeso"],
            y_range=[0, 2000, 500],
            y_length=4,
            x_length=10,
            x_axis_config={"font_size": 36},
        )
        VGroup(chart_number_of_adults, legend_number_of_adults).arrange(
            DOWN).shift(DOWN / 4)
        chart_number_of_adults_bar_lbls = chart_number_of_adults.get_bar_labels(
            color=WHITE, label_constructor=MathTex, font_size=36
        )
        self.play(AddTextLetterByLetter(source_number_of_adults, run_time=0.25),
                  AddTextLetterByLetter(title_number_of_adults, run_time=1))
        self.play(Write(chart_number_of_adults), Write(
            chart_number_of_adults_bar_lbls), FadeIn(legend_number_of_adults))
        playSpinner(self)

        title_porcentage_over_years = MarkupText(
            "<b>Porcentagem de adultos obesos nos EUA</b>", font_size=DEFAULT_FONT_SIZE * 5/6).to_edge(UP)
        source_porcentage_over_years = Text("Fonte: https://www.niddk.nih.gov/health-information/health-statistics/overweight-obesity",
                                            font_size=DEFAULT_FONT_SIZE*1/5).to_corner(LEFT + DOWN)
        legend_porcentage_over_years = Text(
            "Porcentagem de pessoas", font_size=DEFAULT_FONT_SIZE*2/5)
        chart_porcentage_over_years = BarChart(
            values=[30.5, 30.5, 32.2, 34.3, 33.7,
                    35.7, 34.9, 37.7, 39.6, 42.4],
            bar_names=["1999-2000", "2001-2002", "2003-2004", "2005-2006", "2007-2008",
                       "2009-2010", "2011-2012", "2013-2014", "2015-2016", "2017-2018"],
            y_range=[0, 100, 20],
            y_length=5,
            x_length=13,
            x_axis_config={"font_size": 24},
        )
        VGroup(chart_porcentage_over_years, legend_porcentage_over_years).arrange(
            DOWN).shift(DOWN / 4)
        chart_porcentage_over_years_bar_lbls = chart_porcentage_over_years.get_bar_labels(
            color=WHITE, label_constructor=MathTex, font_size=36
        )
        self.play(LaggedStart(Unwrite(chart_number_of_adults), Write(chart_porcentage_over_years), lag_ratio=1.5), LaggedStart(Unwrite(chart_number_of_adults_bar_lbls), Write(
            chart_porcentage_over_years_bar_lbls), lag_ratio=1.5), LaggedStart(FadeOut(legend_number_of_adults), FadeIn(legend_porcentage_over_years), lag_ratio=1.5))
        self.play(ReplacementTransform(source_number_of_adults, source_porcentage_over_years, run_time=0.25),
                  ReplacementTransform(title_number_of_adults, title_porcentage_over_years, run_time=1))
        playSpinner(self)
        fadeAll(self, DOWN)


# %%
#!%%manim -qm Main


class Main(Scene):
    def construct(self):
        Intro.construct(self)
        ObesityDefinition.construct(self)
        Statistics.construct(self)

# %%
