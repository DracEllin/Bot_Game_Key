from sqlalchemy.orm import relationship,mapped_column,Mapped,Session,DeclarativeBase
from sqlalchemy import Integer,String,ForeignKey
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession,AsyncAttrs,async_sessionmaker

from config import MYSQL_URL

engine = create_async_engine(MYSQL_URL, echo=True)

async_session = async_sessionmaker(engine)


class Base(DeclarativeBase,AsyncAttrs):
    pass 


class Category(Base):
    __tablename__ = 'category'

    id:Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    name:Mapped[str] = mapped_column(String(50))

    games = relationship('Game',back_populates="category")


class GameKey(Base):
    __tablename__ = 'game_key'

    id:Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    key:Mapped[str] = mapped_column(String(50))
    count:Mapped[int] = mapped_column(Integer, default=0)
    price:Mapped[int] = mapped_column(Integer, default=0)


    game = relationship('Game',back_populates="key", uselist=False)


class Game(Base):
    __tablename__ = 'game'

    id:Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    name:Mapped[str] = mapped_column(String(50))
    description:Mapped[str] = mapped_column(String(250))
    image:Mapped[str] = mapped_column(String(250))
    category_id:Mapped[int] = mapped_column(ForeignKey('category.id'))
    key_id:Mapped[int] = mapped_column(ForeignKey('game_key.id'), unique=True)

    category = relationship('Category',back_populates="games")
    key = relationship('GameKey',back_populates="game", uselist=False)



async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def add_category():
    async with async_session() as session:
        category = Game(name='Saints Row®: The Third', 
                        description='''The Elder Scrolls V: Skyrim — компьютерная игра в жанре action/RPG открытым миром, разработанная студией Bethesda Game Studios и выпущенная компанией Bethesda Softworks.''',
                        image="database\image\sr.jpg",
                        category_id = 4,
                        key_id=4)
        session.add(category)
        await session.commit()
        await session.refresh(category)
        return category
    
# Grand Theft Auto V Grand Theft Auto V для PC позволяет игрокам исследовать знаменитый мир Лос-Сантоса и округа Блэйн в разрешении до 4k и выше с частотой 60 кадров в секунду.
# Assassin’s Creed® IV Black Flag™ 1715 год, Карибские острова. Пираты стали истинными владыками моря и суши, организовав собственную республику беззакония, жадности и жестокости.Среди этих разбойников заметен юный капитан Эдвард Кенуэй. Репутация драчуна и искателя приключений позволила ему завоева
# Saints Row®: The Third The Full Package Remastered — благодаря улучшенной графике, переработанному освещению, дополненным картам и новым спецэффектам Стилпорт и Святые с Третьей улицы смотрятся еще более впечатляюще, чем раньше.