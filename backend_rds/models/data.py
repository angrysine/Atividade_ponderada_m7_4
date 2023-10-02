from sqlalchemy import  Column, Float, String, Integer, Boolean
from models.base import Base



class AircraftData(Base):
    __tablename__ = 'aircraft_data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    aircraftSerNum_1 = Column(Float)
    phaseOfFlight_1 = Column(Float)
    amscHprsovDrivF_1a = Column(Float)
    amscHprsovDrivF_1b = Column(Float)
    amscHprsovDrivF_2b = Column(Float)
    amscPrsovDrivF_1a = Column(Float)
    amscPrsovDrivF_1b = Column(Float)
    amscPrsovDrivF_2b = Column(Float)
    basBleedLowPressF_1a = Column(Float)
    basBleedLowPressF_2b = Column(Float)
    basBleedLowTempF_1a = Column(Float)
    basBleedLowTempF_2b = Column(Float)
    basBleedOverPressF_1a = Column(Float)
    basBleedOverPressF_2b = Column(Float)
    basBleedOverTempF_1a = Column(Float)
    basBleedOverTempF_2b = Column(Float)
    bleedFavTmCmd_1a = Column(Float)
    bleedFavTmCmd_1b = Column(Float)
    bleedFavTmCmd_2a = Column(Float)
    bleedFavTmCmd_2b = Column(Float)
    bleedFavTmFbk_1a = Column(Float)
    bleedFavTmFbk_1b = Column(Float)
    bleedFavTmFbk_2b = Column(Float)
    bleedHprsovCmdStatus_1a = Column(Float)
    bleedHprsovCmdStatus_1b = Column(Float)
    bleedHprsovCmdStatus_2a = Column(Float)
    bleedHprsovCmdStatus_2b = Column(Float)
    bleedHprsovOpPosStatus_1a = Column(Float)
    bleedHprsovOpPosStatus_1b = Column(Float)
    bleedHprsovOpPosStatus_2a = Column(Float)
    bleedHprsovOpPosStatus_2b = Column(Float)
    bleedMonPress_1a = Column(Float)
    bleedMonPress_1b = Column(Float)
    bleedMonPress_2a = Column(Float)
    bleedMonPress_2b = Column(Float)
    bleedOnStatus_1a = Column(Float)
    bleedOnStatus_1b = Column(Float)
    bleedOnStatus_2b = Column(Float)
    bleedOverpressCas_2a = Column(Float)
    bleedOverpressCas_2b = Column(Float)
    bleedPrecoolDiffPress_1a = Column(Float)
    bleedPrecoolDiffPress_1b = Column(Float)
    bleedPrecoolDiffPress_2a = Column(Float)
    bleedPrecoolDiffPress_2b = Column(Float)
    bleedPrsovClPosStatus_1a = Column(Float)
    bleedPrsovClPosStatus_2a = Column(Float)
    date = Column(String)
    duration = Column(Float)
 
    cumulative_duration = Column(Float)

    time_to_failure = Column(Float)




