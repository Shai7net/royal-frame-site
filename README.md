# Royal Frame website

Public static website for Royal Frame, including the product home page, support information,
privacy policy, terms of use and account-deletion instructions.

Live site: <https://shai7net.github.io/royal-frame-site/>

Microsoft Store fields:

- Website: <https://shai7net.github.io/royal-frame-site/>
- Support contact: <https://shai7net.github.io/royal-frame-site/support.html>
- Privacy policy: <https://shai7net.github.io/royal-frame-site/privacy.html>

The site contains no analytics, cookies, build step or external runtime dependency. It is designed
to be served directly by GitHub Pages from the `main` branch root.

## Download destinations

The home-page download center deliberately presents four device choices while keeping the actual
distribution model accurate:

- Windows uses the latest public `RoyalFrameSetup.exe` release.
- Apple opens the installable web controller at <https://royal-frame-remote.web.app>; there is no
  native App Store build yet.
- Android phone/tablet and Android TV have separate instruction cards but use the same Play package,
  `net.shai7.royalframe`.
- While the Play release is in closed testing, both Android cards start at the tester opt-in URL.
  The TV instructions use Google Play's remote-device picker so testers do not type URLs with a TV
  remote.

## Local preview

Serve this directory with any static HTTP server and open `index.html`. Do not rely on `file://`
for final verification because browser behavior differs from a real origin.

## Public contact

Royal Frame is developed and operated by Shai Tiri and distributed under the HayotzerAI brand.
Support and privacy requests use `shai7net@gmail.com`.
