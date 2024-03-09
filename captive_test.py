import captive
import uasyncio as asyncio

print('Captive Test')

try:
    # Instantiate app and run
    myapp = captive.MyApp(essid='captive test wifi')
    print('run', myapp)
    asyncio.run(myapp.start())

except KeyboardInterrupt:
    print('Bye')

finally:
    asyncio.new_event_loop()  # Clear retained state