// Sam Alptekin
// Web scraper implementation in C++ that pulls data from the south bend open
// data website

#include <iostream>         // cin and cout
#include <string>           // strings
#include <curl/curl.h>      // implementing curl
//#include <libtidy>
//#include <libxml>

using namespace std;

CURLcode get(string);

int main(){

  string url = "http://data-southbend.opendata.arcgis.com/datasets/b943dc9a3bb34808a0b8f99f62bb5306_0?uiTab=table";
  CURLcode res;
  
  res = get(url);
}

// implementation of curl using libcurl (#include <curl/curl.h>)
CURLcode get(string url){

  CURL *curl;

  curl = curl_easy_init();

  if(curl) {
    curl_easy_setopt(curl, CURLOPT_URL, url.c_str());

    curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L);


    return curl_easy_perform(curl);

    curl_easy_cleanup(curl);
  }
}
