let url = new URL(window.location);
let params  = url.searchParams;

let confirmation = document.querySelector(".join-confirm");
let params_list = ['fname','lname','title','email','cellphone','bizname','websiteURL','level','description']    
let description_list = ['First Name:','Last Name:','Title:','E-mail:','Cellphone','Business Name:','Website URL:','Membership Level:','Business Description:']

let build_string = "<table>";
for (i=0; i < params_list.length; i++){
  key = description_list[i]
  value = params.get(params_list[i])
  if (value == null){
    value = ''
  }
  build_string += `<tr><td class="right-justify">${key}</td><td class="left-justify">${value}</td></tr>`
}
let now1 = new Date()
let today = new Intl.DateTimeFormat("en-US", { dateStyle: "short" }).format(  );
build_string += `<tr><td class="right-justify">Signup Date: </td><td class="left-justify">${today}</td></tr>`
build_string += "</table>"
confirmation.innerHTML = build_string