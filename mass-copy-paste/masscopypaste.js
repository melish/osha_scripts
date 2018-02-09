// see https://jira.osha.europa.eu/browse/CW-1847

var fields = {};
jQuery("form").find("textarea").each(function(idx, elem) {
  fields[elem.getAttribute("id")] = elem.innerHTML;
});
console.log(JSON.stringify(fields));

/////////////////////////////////////

var json = {"edit-translations-bg":"Носител на награда 2009","edit-translations-cs":"Vítěz soutěže 2009","edit-translations-da":"Prisvinder 2009","edit-translations-de":"Preisträger 2009","edit-translations-el":"Νικητής του βραβείου 2009","edit-translations-es":"Ganador del galardón 2009","edit-translations-et":"Auhinna võitja 2009","edit-translations-fi":"Palkinnon voittaja 2009","edit-translations-hr":"Dobitnik nagrade 2009","edit-translations-fr":"Lauréat 2009","edit-translations-hu":"2009. évi díjazott","edit-translations-is":"Sigurvegari verðlauna 2009","edit-translations-it":"Vincitore del premio 2009","edit-translations-lv":"2009.gada balvas ieguvējs ","edit-translations-lt":"Apdovanojimo laimėtojas 2009","edit-translations-nl":"Prijswinnaar 2009","edit-translations-mt":"Rebbieħ tal-premju 2009","edit-translations-no":"Prisvinner 2009","edit-translations-pl":"Laureat nagrody 2009","edit-translations-pt":"Vencedor do Prémio 2009","edit-translations-ro":"Câștigătorul premiului 2009","edit-translations-sk":"Víťaz ceny 2009","edit-translations-sl":"Prejemnik nagrade 2009","edit-translations-sv":"Prisvinnare 2009","edit-translations-sq":"","edit-translations-bs":"","edit-translations-mk":"","edit-translations-ru":"","edit-translations-sr":"","edit-translations-sh":"","edit-translations-tr":""}
jQuery("form").find("textarea").each(function(idx, elem) {
  elem.innerHTML = json[elem.getAttribute("id")];
});
