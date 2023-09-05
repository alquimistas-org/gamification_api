from datetime import date

from sqlalchemy import CheckConstraint, Column
from sqlalchemy import Enum as SqlAlchemyEnum
from sqlalchemy import ForeignKey, Table
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from utils import Status, UserRole


class Base(DeclarativeBase):
    ...


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    active: Mapped[bool] = mapped_column(default=False)
    role: Mapped[str] = mapped_column(SqlAlchemyEnum(UserRole), default=UserRole.USER)


class Metric(Base):
    __tablename__ = "metrics"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True)


class Challenge(Base):
    __tablename__ = "challenges"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_challenger: Mapped["User"] = relationship(back_populates="challenges")
    user_challenged: Mapped["User"] = relationship(back_populates="challenges")
    tournament: Mapped["Tournament"] = relationship(back_populates="challenges")


class Tournament(Base):
    __tablename__ = "tournaments"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True)
    start_date: Mapped[date]
    end_date: Mapped[date]
    status: Mapped[str] = mapped_column(SqlAlchemyEnum(Status), default=Status.ACTIVE)
    CheckConstraint("start_date < end_date", name="check_start_end_dates")


association_user_and_metric_history = Table(
    "association_user_and_metric_history",
    Base.metadata,
    Column("metric_daily_history_id", ForeignKey("metrics_daily_history.id")),
    Column("user_id", ForeignKey("users.id")),
)

association_metric_and_metric_history = Table(
    "association_metric_and_metric_history",
    Base.metadata,
    Column("metric_daily_history_id", ForeignKey("metrics_daily_history.id")),
    Column("metric_id", ForeignKey("metrics.id")),
)

association_challenge_and_metric_history = Table(
    "association_challenge_and_metric_history",
    Base.metadata,
    Column("metric_daily_history_id", ForeignKey("metrics_daily_history.id")),
    Column("challenge_id", ForeignKey("challenges.id")),
)


class MetricDailyHistory(Base):
    __tablename__ = "metrics_daily_history"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[list["User"]] = relationship(secondary=association_user_and_metric_history)
    metric_id: Mapped[list["Metric"]] = relationship(secondary=association_metric_and_metric_history)
    score: Mapped[int]
    date: Mapped[date]
    challenge_id: Mapped[list["Challenge"]] = relationship(secondary=association_challenge_and_metric_history)
