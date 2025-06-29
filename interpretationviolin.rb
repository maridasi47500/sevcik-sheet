require 'watir'

browser = Watir::Browser.new :firefox
browser.goto('https://imslp.org/wiki/School_of_Interpretation_for_the_Violin,_Op.16_(%C5%A0ev%C4%8D%C3%ADk,_Otakar)')
original_window = browser.driver.window_handle

browser.execute_script(<<-JS)
  const pdfLinks = Array.from(document.querySelectorAll('a'))
    .map(link => link.href)
    .filter(href => href.includes('Special:ImagefromIndex'));

  pdfLinks.forEach((link, index) => {
    setTimeout(() => {
      window.open(link, '_blank');
    }, index * 1000);
  });
JS
window_handles = browser.driver.window_handles

# Parcourir chaque fenêtre une par une
window_handles.each do |handle|
  browser.driver.switch_to.window(handle)
  # Injecter du JavaScript dans la page chargée
  browser.execute_script(<<-JS)
    const pdfLinks = Array.from(document.querySelectorAll('a'))
      .map(link => link.href)
      .filter(href => href.includes('Special:IMSLPDisclaimerAccept'));
  
    pdfLinks.forEach((link, index) => {
      setTimeout(() => {
        link.click();
      }, index * 1000);
    });
  JS
  puts "🔍 Titre de l'onglet : #{browser.title}"
  sleep 2  # pause pour que tu vois la bascule
end

# Retour à la première fenêtre
browser.driver.switch_to.window(window_handles.first)


