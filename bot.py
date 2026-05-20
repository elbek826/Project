from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup
import logging
import asyncio
from aiogram import Bot,Dispatcher,types,F
from aiogram.filters import Command
from buttons import share_contact
from Database import show_users,add_to_db
class RegState(StatesGroup):
    name=State()
    phone=State()
    address=State()
admin_id=7645264588
api = '7850708922:AAEixcaYYihQLTQ96NImAXZlVKN1pbB6W6M'
bot = Bot(api)
dp=Dispatcher()

async def main():
    await dp.start_polling(bot)
@dp.message(Command('start'))
async def start(sms:types.Message):
    if admin_id==sms.from_user.id:
        await sms.answer(text='HELLO ELbek!')
    else:
        await sms.answer(text='''HELLo
                        Registratsiya qiliw ushin registration deb jazin!''')
@dp.message(F.text=='registration')
async def send_name(sms:types.Message,state:FSMContext):
    await sms.answer(text="Regstratsiyani baslaw ushin atinizdi jazin!")
    await state.set_state(RegState.name)
@dp.message(RegState.name)
async def send_phone(sms:types.Message,state:FSMContext):
    await state.update_data(ati=sms.text)
    await sms.answer(text='Nomerinizdi jazin',reply_markup=share_contact)
    await state.set_state(RegState.phone)
@dp.message(RegState.phone)
async def send_adress(sms:types.Message,state:FSMContext):
    await state.update_data(nomer=sms.contact.phone_number)
    await sms.answer(text='Endi addressinizdi jazin!')
    await state.set_state(RegState.address)
@dp.message(RegState.address)
async def save(sms:types.Message,state:FSMContext):
    await state.update_data(address=sms.text)
    datas=await state.get_data()
    await state.clear()
    await add_to_db(
        id=sms.from_user.id,
        name=datas['ati'],
        phone=datas['nomer'],
        address=datas['address']
    )
if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
