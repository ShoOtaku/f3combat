FFxivPythonTrigger3 combat strategy

---

To use my combat strategy, please make sure your FPT3 is up to date

How to add a new strategy to your XivCombat

* put the folder **meta_data** into .\\FFxivPythonTrigger\
* put the strategy into .\plugins\XivCombat\strategies\OT
* add the job your just put in the folder like below in **_init_.py**

> from .monk import MonkStrategy

* reload XivCombat and try

**Any question or advice is welcome**

**Current FCR Status:**

**MNK:** Almost Complete [need opt a lot]

**DRG:** complete

**BLM**: complete except dot and foul/xeon (haven't tested above lv 70)

known issue:

blm will cast twice thunder when need dot
