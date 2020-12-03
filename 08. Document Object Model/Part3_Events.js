var hone = document.querySelector('#one')
var htwo = document.querySelector('#two')
var hthree = document.querySelector('#three')

console.log('connected')


hone.addEventListener('mouseover', function(){
  hone.textContent = 'Mouse currently OVER'
  hone.style.color = 'red'
})

hone.addEventListener('mouseout', function(){
  hone.textContent  = 'Mouse Over Me!'
  hone.style.color = 'black'
})

htwo.addEventListener('click', function(){
  htwo.textContent = 'clicked!!'
  htwo.style.color = 'red'
})

hthree.addEventListener('dblclick', function(){
  hthree.textContent = 'DOUBLE'
  hthree.style.color = 'hotpink'
})